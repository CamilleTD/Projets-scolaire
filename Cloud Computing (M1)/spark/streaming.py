from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("DrugSafetyStreaming") \
    .config("spark.sql.streaming.checkpointLocation", "/tmp/checkpoint") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

schema = StructType([
    StructField("report_id",         StringType(),  True),
    StructField("report_date",       StringType(),  True),
    StructField("drug_name",         StringType(),  True),
    StructField("drug_class",        StringType(),  True),
    StructField("adverse_event",     StringType(),  True),
    StructField("severity",          StringType(),  True),
    StructField("outcome",           StringType(),  True),
    StructField("age_group",         StringType(),  True),
    StructField("country",           StringType(),  True),
    StructField("manufacturer",      StringType(),  True),
    StructField("source_type",       StringType(),  True),
    StructField("seriousness_score", IntegerType(), True),
])


streamDF = spark.readStream \
    .format("csv") \
    .option("header", "true") \
    .schema(schema) \
    .load("/opt/spark-app/data/stream/")


streamDF = streamDF.withColumn("severity_num",
    F.when(F.col("severity") == "Mild",     1)
     .when(F.col("severity") == "Moderate", 2)
     .when(F.col("severity") == "Severe",   3)
     .when(F.col("severity") == "Critical", 4)
     .otherwise(1))

drug_counts = streamDF.groupBy("drug_name") \
    .agg(
        F.count("*").alias("total_reports"),
        F.avg("seriousness_score").alias("avg_seriousness"),
        F.sum(F.when(F.col("severity").isin(["Severe", "Critical"]), 1).otherwise(0)).alias("severe_count")
    )


query = drug_counts.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", False) \
    .trigger(processingTime="10 seconds") \
    .start()

print("\nSTREAMING STARTED — Watching /opt/spark-app/data/stream/")
print("Drop CSV files into spark/data/stream/ to see real-time updates\n")

query.awaitTermination()