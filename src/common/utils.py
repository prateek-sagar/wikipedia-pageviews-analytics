# helper functions

from pathlib import Path
import yaml # type: ignore
from pyspark.sql import SparkSession, DataFrame # type: ignore
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, LongType # type: ignore
from pyspark.sql.functions import explode, col # type: ignore
from functools import wraps
from src.storage.lakehouse_writer import evidence_writer

 

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = PROJECT_ROOT / 'configs'


def load_yaml_config(filename: str) -> dict:
    config_path = CONFIG_DIR / filename
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def provide_spark_engine() -> SparkSession:
    return SparkSession.builder.appName("Wikipedia Pageview Project").getOrCreate()

def read_data_and_apply_schema(data: dict, engine: SparkSession) -> DataFrame:

    if (not data):
        raise RuntimeError(f"The Data is Empty")

    _schema = schema()

    df = engine.createDataFrame(data, schema=_schema)

    normalised_df = (df.select(explode(col('items')).alias("item")).select("item.*"))
    
    return normalised_df



def schema() -> StructType:

    itemSchema = StructType([
       StructField("project", StringType(), True),
       StructField("access", StringType(), True),
       StructField("agent", StringType(), True),
       StructField("granularity", StringType(), True),
       StructField("timestamp", StringType(), True),
       StructField("views", LongType(), True)
   ])


    rootSchema = StructType([
        StructField("items", ArrayType(itemSchema), True)
    ])
    return rootSchema

