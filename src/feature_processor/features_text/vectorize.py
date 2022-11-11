import os
from pyspark.sql import DataFrame, Row, SparkSession, types


def _ParseLine(line: str) -> Row:
    parts = line.split(sep=" ")

    word = parts[0]

    embedding = list()
    for i in range(1, len(parts)):
        embedding.append(float(parts[i]))

    return Row(word=word, embedding=embedding)


def LoadGloveDefinitions(path: str,
                         dimension: int,
                         spark: SparkSession) -> DataFrame:
    """Loads GloVe word embeddings definitions as a dataframe.

    Example output:
    --------------------------------------------
    | word  | embedding                        |
    --------------------------------------------
    | "the" | [0.418, 0.24968, -0.41242, ...]  |
    --------------------------------------------
    | "won" | [-1.5561, 0.86241, 0.14604, ...] |
    --------------------------------------------

    Args:
        path (str): Path to which GloVe word embeddings txt files are located.
        dimension (int): The size of word embeddins to use. Value can be 50,
            100, 200 and 300.

    Returns:
        DataFrame: See the example output above.
    """
    glove_file_name = "glove.6B.{0}d.txt".format(dimension)
    glove_path = os.path.join(path, glove_file_name)

    schema = types.StructType(
        fields=[
            types.StructField(
                name="word", dataType=types.StringType()),
            types.StructField(
                name="embedding", dataType=types.ArrayType(
                    elementType=types.FloatType()))
        ])

    return spark.                   \
        sparkContext.               \
        textFile(name=glove_path).  \
        map(_ParseLine).            \
        toDF(schema=schema)


def VectorizeContentTokens(content_tokens: DataFrame,
                           term_idf: DataFrame,
                           glove: DataFrame) -> DataFrame:
    """_summary_

    Args:
        content_tokens (DataFrame): _description_
        term_idf (DataFrame): _description_
        glove (DataFrame): _description_

    Returns:
        DataFrame: _description_
    """
    pass


def VectorizeContentGenomeScores(content_tokens: DataFrame,
                                 term_idf: DataFrame,
                                 glove: DataFrame) -> DataFrame:
    """_summary_

    Args:
        content_tokens (DataFrame): _description_
        term_idf (DataFrame): _description_
        glove (DataFrame): _description_

    Returns:
        DataFrame: _description_
    """
    pass


def VectorizeUserTokens(user_tag_tokens: DataFrame,
                        glove: DataFrame) -> DataFrame:
    """_summary_

    Args:
        user_tag_tokens (DataFrame): _description_
        glove (DataFrame): _description_

    Returns:
        DataFrame: _description_
    """
    pass