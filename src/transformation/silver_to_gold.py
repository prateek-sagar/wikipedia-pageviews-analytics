from pyspark.sql import DataFrame # type: ignore

def silver_to_gold(dataframe: DataFrame):
    if (dataframe is None):
        return
    
    # aggregation
    # split