from  pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import to_timestamp, col

def casting(df:DataFrame, engine: SparkSession):
    """
    Docstring for casting
    
    :param df: Description
    :type df: DataFrame
    :param engine: Description
    :type engine: SparkSession
    """

    df = df.withColumn(
        "timestamp", to_timestamp(col("timestamp"), "yyyyMMddHH")
    )

    return df

    