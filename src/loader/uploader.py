import logging
import grpc

from math import ceil
from pyspark import RDD, Row
from pyspark.sql import DataFrame
from typing import Any, Iterable, List

__CONNECTION_REUSE = 39


class RecordUploaderConnection:
    """Stores a gRPC channel and a client stub.
    """

    def __init__(self, channel: grpc.Channel, stub: object) -> None:
        self.channel = channel
        self.stub = stub


class RecordUploaderInterface:
    """All class implementations must be stateless. The derived classes should
    expect that it is going to be broadcasted and invoked in executors.
    """

    def MaxBatchSize(self) -> int:
        """The maximum number of records it can upload at a time.

        Returns:
            int: Must be greater than 0.
        """
        return 1

    def Connect(self) -> RecordUploaderConnection:
        """Creates a connection to the target server.

        Returns:
            RecordUploaderConnection: See above.
        """
        return None

    def UploadBatch(self,
                    batch: List[Row],
                    connection: RecordUploaderConnection) -> bool:
        """Uploads the batch of records through the specified connection.

        Args:
            batch (List[Row]): The batch of records to be uploaded.
            connection (RecordUploaderConnection): Created from the 
                self.Connect() call

        Returns:
            bool: Indicates whether the upload was successful.
        """
        return False


def __UploadPartition(
        partition: Iterable[Row],
        uploader: RecordUploaderInterface) -> Iterable[Any]:
    connection = uploader.Connect()
    if connection is None:
        for failed_record in partition:
            yield failed_record
        return

    # Keeps the connection alive and uploads the entire partition in
    # batches.
    batch = list()

    for row in partition:
        # Collects a new batch of records.
        batch.append(row)

        if len(batch) < uploader.MaxBatchSize():
            continue

        # Uploads the current batch of records.
        if not uploader.UploadBatch(batch=batch, connection=connection):
            for failed_record in batch:
                yield failed_record

        batch.clear()

    # Uploads the last batch of records from the partition if there is any.
    if len(batch) == 0:
        return

    if not uploader.UploadBatch(batch=batch, connection=connection):
        for failed_record in batch:
            yield failed_record


def UploadDataFrame(data_frame: DataFrame,
                    uploader: RecordUploaderInterface,
                    num_retries: int) -> DataFrame:
    """Uploads a generic data frame via RPCs. It properly partitions the
    underlying RDD and uploads row recordsd in batches.

    Args:
        data_frame (DataFrame): The generic data frame to be uploaded.
        uploader (RecordUploaderInterface): Defines the network connection and
            how each batch of records are sent.
        num_retries (int): The maximum number of time where failed uploads are
            retried. Must be greater than or equal to 0.

    Returns:
        DataFrame: A data frame which contains the collection of records that
            failed to be uploaded after the specified number of retries.
    """
    failed_uploads = data_frame.rdd

    for retry in range(num_retries + 1):
        num_records_per_upload = uploader.MaxBatchSize()
        num_records_per_partition = num_records_per_upload * \
            (1 + __CONNECTION_REUSE)
        num_partitions = ceil(failed_uploads.count()/num_records_per_partition)

        logging.info(
            "UploadDataFrame(): retry={retry} num_partitions={num_partitions}".format(
                retry=retry, num_partitions=num_partitions))

        failed_uploads = failed_uploads.\
            repartition(numPartitions=num_partitions).\
            mapPartitions(lambda p: __UploadPartition(p, uploader)).\
            cache()

        if failed_uploads.count() == 0:
            break

    logging.info(
        "UploadDataFrame(): upload finished. Returning failed records, if there is any.")
    return failed_uploads.toDF(schema=data_frame.schema)
