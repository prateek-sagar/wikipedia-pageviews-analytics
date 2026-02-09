from pyspark.sql import DataFrame, SparkSession

class PostgreReadWrite:
    DRIVER = "org.postgresql.Driver"

    def __init__(self, spark: SparkSession,  host, user, password, db, batchSize = 4, numPartitions = 10000):
        self.__properties = {
            "user": user,
            "password": password,
            "driver": self.DRIVER,
            "batchsize": str(batchSize),
        }
        self.__spark = spark
        self.__url = f"jdbc:postgresql://{host}:5432/{db}"

    def read(self, table: str) -> DataFrame:
        return self.__spark.read.jdbc(self.__url, table=table, properties=self.__properties)

    def write(self, df: DataFrame, table: str, mode: str = "overwrite"):

        if mode not in ("append", "overwrite"):
            raise ValueError("Mode must be either append or overwrite")

        if df.rdd.isEmpty():
            print(f"[INFO] No new rows to insert into {table}. Skipping write.")
            return

        try:
            df.write.mode(mode).jdbc(self.__url, table, properties=self.__properties)
        except Exception as e: 
            raise RuntimeError(f" Failed to write data into {table}") from e