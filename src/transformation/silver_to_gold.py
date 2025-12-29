from pyspark.sql import DataFrame


def silver_to_gold(dataframe: DataFrame):
    if (dataframe is null):
        return
    
    # aggregation
    # split