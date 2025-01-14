from pyspark.sql import DataFrame


def CollectContentText(contents: DataFrame,
                       spell_correction: bool) -> DataFrame:
    """Collects textual information for each piece of content from the content
    dataframe.

    Example input:
    -----------------------------------------------------
    | id | title     | tmdb_primary_info                |
    -----------------------------------------------------
    | 1  | "A title" | '{                               |
    |    |           |      "overview": "An overveiw.", |
    |    |           |      "tagline": "A tagline",     |
    |    |           |  }'                              |
    -----------------------------------------------------
    | 2  | '{}'                                         |
    -----------------------------------------------------
    | 3  | '{"overview": ""}'                           |
    -----------------------------------------------------

    Example output:
    -----------------------
    | id | text           |
    -----------------------
    | 1  | "A title.      |
    |    |  An overview.  |
    |    |  A tagline."   |
    -----------------------

    Args:
        contents (DataFrame): See the example input above.
        spell_correction (bool): Whether to perform spell correction to the
            text.

    Returns:
        DataFrame: See the example output above.
    """
    contents.show()


def CollectContentTags(contents: DataFrame,
                       spell_correction: bool) -> DataFrame:
    """Turns the user tag JSON string into a line of string with each tag
    separated by comma.

    Example input:
    --------------------------------------------
    | id | tags                                |
    --------------------------------------------
    | 1  | '[{                                 |
    |    |      "tag": "unlikely friendships", |
    |    |      "timestamp_secs": 1438711374   |
    |    |  },                                 |
    |    |  {                                  |
    |    |      "tag": "Buzz Lightyear",       |
    |    |      "timestamp_secs": 1140447535   |
    |    |  }]'                                |
    --------------------------------------------
    | 2  | '[]'                                |
    --------------------------------------------


    Example output:
    ----------------------------------------------
    | id | text                                  |
    ----------------------------------------------
    | 1  | "unlikely friendships,Buzz Lightyear" |
    ----------------------------------------------

    Args:
        contents (DataFrame): See the example input above.
        spell_correction (bool): Whether to perform spell correction to the
            text.

    Returns:
        DataFrame: See the example output above.
    """
    contents.show()


def TokenizeText(content_text: DataFrame) -> DataFrame:
    """Breaks a text string into word tokens for each piece of content.

    Example input:
    -----------------------
    | id | text           |
    -----------------------
    | 1  | "An overview." |
    -----------------------

    Example output:
    --------------------------------
    | id | index | token           |
    --------------------------------
    | 1  | 0     | "an"            |
    --------------------------------
    | 1  | 1     | "overview"      |
    --------------------------------
    | 1  | 2     | "."             |
    --------------------------------

    Args:
        content_text (DataFrame): See the example input above.

    Returns:
        DataFrame: See the example output above.
    """
    content_text.show()


def CollectTerms(content_tokens: DataFrame) -> DataFrame:
    """Collects fine grain word pieces that we care about and find their
    stemmed form. Words that we don't care about are: punctuations, stopwords
    and people names. Big word pieces are continued to be broken down by
    punctuation.

    Example input:
    ------------------------
    | id | token           |
    ------------------------
    | 1  | "anna"          |
    ------------------------
    | 1  | ","             |
    ------------------------
    | 1  | "an"            |
    ------------------------
    | 1  | "oh-my-god"     |
    ------------------------
    | 1  | "moment"        |
    ------------------------
    | 1  | "."             |
    ------------------------

    Example output:
    -----------------------------------
    | id | token           | term     |
    -----------------------------------
    | 1  | "anna"          | NULL     |
    -----------------------------------
    | 1  | ","             | NULL     |
    -----------------------------------
    | 1  | "an"            | NULL     |
    -----------------------------------
    | 1  | "oh-my-god"     | "oh"     |
    -----------------------------------
    | 1  | "oh-my-god"     | "god"    |
    -----------------------------------
    | 1  | "moment"        | "moment" |
    -----------------------------------
    | 1  | "."             | NULL     |
    -----------------------------------

    Args:
        content_tokens (DataFrame): See the example input above.

    Returns:
        Tuple[DataFrame, DataFrame]: See the example output above.
    """
    content_tokens.show()


def ComputeIdf(content_tokens_terms: DataFrame) -> DataFrame:
    """Computes the inverse document frequency for the tokens in each piece of
    content.

    A token's IDF is determined by the maximum IDF of its composition term. For
    example, a word token "oh-my-god" consists of 2 terms: oh and god.
    The IDF of the word token is therefore:
        word_idf("oh-my-god") = max(term_idf("oh"), term_idf("god"))

    Example input:
    -----------------------------------
    | id | token           | term     |
    -----------------------------------
    | 1  | "anna"          | NULL     |
    -----------------------------------
    | 1  | ","             | NULL     |
    -----------------------------------
    | 1  | "an"            | NULL     |
    -----------------------------------
    | 1  | "oh-my-god"     | "oh"     |
    -----------------------------------
    | 1  | "oh-my-god"     | "god"    |
    -----------------------------------
    | 1  | "moment"        | "moment" |
    -----------------------------------
    | 1  | "."             | NULL     |
    -----------------------------------

    Intermediate result (term IDF):
    -----------------------------------------
    | id | token           | term     | idf |
    -----------------------------------------
    | 1  | "anna"          | NULL     | 0   |
    -----------------------------------------
    | 1  | ","             | NULL     | 0   |
    -----------------------------------------
    | 1  | "an"            | NULL     | 0   |
    -----------------------------------------
    | 1  | "oh-my-god"     | "oh"     | 0.5 |
    -----------------------------------------
    | 1  | "oh-my-god"     | "god"    | 1.2 |
    -----------------------------------------
    | 1  | "moment"        | "moment" | 0.8 |
    -----------------------------------------
    | 1  | "."             | NULL     | 0   |
    -----------------------------------------

    Example output:
    ------------------------------
    | id | token           | idf |
    ------------------------------
    | 1  | "anna"          | 0   |
    ------------------------------
    | 1  | ","             | 0   |
    ------------------------------
    | 1  | "an"            | 0   |
    ------------------------------
    | 1  | "oh-my-god"     | 1.2 |
    ------------------------------
    | 1  | "moment"        | 0.8 |
    ------------------------------
    | 1  | "."             | 0   |
    ------------------------------


    Args:
        content_tokens_terms (DataFrame): See the example input above.

    Returns:
        DataFrame: See the example output above.
    """
    content_tokens_terms.show()
