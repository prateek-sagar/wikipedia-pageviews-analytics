from pyspark.sql import DataFrame, SparkSession # type: ignore
from common.decorators import observable


@observable("cleaning")
def cleaning(df: DataFrame, engine: SparkSession, *, run_id, window):
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

    return df

    

