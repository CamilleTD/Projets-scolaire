from pyspark.sql import functions as F
from pymongo import MongoClient


def store_to_mongo(spark, df):
    """Stores Spark results in MongoDB."""


    top_drugs = df.groupBy("drug_name").count() \
                  .orderBy("count", ascending=False) \
                  .toPandas().to_dict("records")


    df2 = df.withColumn("severity_num",
        F.when(F.col("severity") == "Mild",     1)
         .when(F.col("severity") == "Moderate", 2)
         .when(F.col("severity") == "Severe",   3)
         .when(F.col("severity") == "Critical", 4)
         .otherwise(1))

    risk_scores = df2.groupBy("drug_name").agg(
        F.count("*").alias("nb_reports"),
        F.avg("seriousness_score").alias("avg_seriousness"),
        F.avg("severity_num").alias("avg_severity_num")
    ).withColumn(
        "risk_score",
        F.round(F.col("nb_reports") * F.col("avg_seriousness") * F.col("avg_severity_num"), 2)
    ).orderBy("risk_score", ascending=False).toPandas().to_dict("records")


    hospitalizations = df.filter(F.col("outcome") == "Hospitalized") \
        .groupBy("drug_name") \
        .count() \
        .withColumnRenamed("count", "hospitalization_count") \
        .orderBy("hospitalization_count", ascending=False) \
        .toPandas().to_dict("records")


    client = MongoClient("mongodb://mongodb:27017/")
    db = client["pharmacovigilance"]

    db["top_drugs"].drop()
    db["top_drugs"].insert_many(top_drugs)

    db["risk_scores"].drop()
    db["risk_scores"].insert_many(risk_scores)

    db["hospitalizations"].drop()
    db["hospitalizations"].insert_many(hospitalizations)

    print("Results stored in MongoDB successfully!")
    print(f"   → top_drugs       : {len(top_drugs)} documents")
    print(f"   → risk_scores     : {len(risk_scores)} documents")
    print(f"   → hospitalizations: {len(hospitalizations)} documents")

    client.close()


if __name__ == "__main__":
    from pyspark.sql import SparkSession

    spark = SparkSession.builder \
        .appName("StoreResults") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    df = spark.read.csv("/opt/spark-app/data/adverse_events.csv",
                        header=True, inferSchema=True)

    store_to_mongo(spark, df)
    spark.stop()