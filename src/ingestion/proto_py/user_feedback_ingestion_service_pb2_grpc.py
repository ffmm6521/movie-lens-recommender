# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import user_feedback_ingestion_service_pb2 as user__feedback__ingestion__service__pb2


class UserFeedbackIngestionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RecordRatingFeedbacks = channel.unary_unary(
                '/e8.UserFeedbackIngestion/RecordRatingFeedbacks',
                request_serializer=user__feedback__ingestion__service__pb2.RecordRatingFeedbacksRequest.SerializeToString,
                response_deserializer=user__feedback__ingestion__service__pb2.RecordRatingFeedbacksResponse.FromString,
                )


class UserFeedbackIngestionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RecordRatingFeedbacks(self, request, context):
        """Records a list of user feedbacks to pieces of content. It overwrites any
        existing entries keyed by (user_id, content_id).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserFeedbackIngestionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RecordRatingFeedbacks': grpc.unary_unary_rpc_method_handler(
                    servicer.RecordRatingFeedbacks,
                    request_deserializer=user__feedback__ingestion__service__pb2.RecordRatingFeedbacksRequest.FromString,
                    response_serializer=user__feedback__ingestion__service__pb2.RecordRatingFeedbacksResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'e8.UserFeedbackIngestion', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserFeedbackIngestion(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RecordRatingFeedbacks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/e8.UserFeedbackIngestion/RecordRatingFeedbacks',
            user__feedback__ingestion__service__pb2.RecordRatingFeedbacksRequest.SerializeToString,
            user__feedback__ingestion__service__pb2.RecordRatingFeedbacksResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
