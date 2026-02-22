# %%
"""
PS-01: PySpark Basics (Local Mode)

Purpose:
- Initialize Spark session
- Load existing processed CSV
- Understand lazy evaluation
"""

import logging
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

from config import PROCESSED_DATA

# %%
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# %%
def create_spark_session() -> SparkSession:
    """
    Create local Spark session.

    local[*] = use all available CPU cores.
    """
    return (
        SparkSession.builder
        .appName("DataEngineeringV2")
        .master("local[*]")
        .getOrCreate()
    )

# %%
if __name__ == "__main__":
    logging.info("Starting Spark session")

    spark = create_spark_session()

    DATA_FILE = PROCESSED_DATA / "processed_data.csv"

    df = spark.read.csv(str(DATA_FILE),
        header=True,
        inferSchema=True
    )

    logging.info("Schema:")
    df.printSchema()

    logging.info("Showing data:")
    df.show()

    spark.stop()
    logging.info("Spark session stopped")

# %%
