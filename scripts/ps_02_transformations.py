# %%
"""
PS-02: Spark Transformations

Purpose:
- Practice filtering, selecting, grouping
- Map SQL concepts to Spark
- Understand transformations vs actions
"""

import logging
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count

from config import PROCESSED_DATA

# %%
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# %%
def create_spark_session():
    return (
        SparkSession.builder
        .appName("DE_v2_Transformations")
        .master("local[*]")
        .getOrCreate()
    )

# %%
if __name__ == "__main__":
    spark = create_spark_session()

    DATA_FILE = PROCESSED_DATA / "processed_data.csv"

    df = spark.read.csv(str(DATA_FILE),
        header=True,
        inferSchema=True
    )

    logging.info("Original Data")
    df.show()

    # ----------------------------
    # 1. Filtering (SQL: WHERE)
    # ----------------------------
    logging.info("Users age > 30")

    df_filtered = df.filter(col("age") > 30)
    df_filtered.show()

    # ----------------------------
    # 2. Selecting columns
    # ----------------------------
    logging.info("Selecting specific columns")

    df_selected = df.select("name", "city", "age")
    df_selected.show()

    # ----------------------------
    # 3. Aggregation (SQL: GROUP BY)
    # ----------------------------
    logging.info("Users per city")

    df_grouped = (
        df.groupBy("city")
          .agg(
              count("*").alias("user_count"),
              avg("age").alias("avg_age")
          )
    )

    df_grouped.show()

    # ----------------------------
    # 4. All in one
    # ----------------------------
    logging.info("All in one")

    df_allinone = df.select("name", "city", "age").filter(col("age")>30).groupBy("city").agg(count("*").alias("user_count_aio"), avg("age").alias("avg_age_aio"))

    df_allinone.show()

    spark.stop()
# %%
