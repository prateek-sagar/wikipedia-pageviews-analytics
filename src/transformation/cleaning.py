from pyspark.sql import DataFrame, SparkSession # type: ignore


def cleaning(df: DataFrame, engine: SparkSession):
    """
    Here we are dealing with
    null checking,
    duplicate,
    """

    if df.isEmpty():
        raise RuntimeError("DataFrame is empty")

    before_rows = df.count()

    # remove duplicates
    df = df.dropDuplicates()

    # drop rows that break reality
    df = df.dropna(subset=["project", "timestamp", "views"])

    # repair optional uncertainty
    df = df.fillna({
        "agent": "unknown",
        "access": "unknown"
    })

    after_rows = df.count()

    return df, {
        "rows_before": before_rows,
        "rows_after": after_rows,
        "rows_dropped": before_rows - after_rows
    }

    

