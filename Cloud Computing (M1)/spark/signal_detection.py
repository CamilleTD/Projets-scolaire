from pyspark.sql import functions as F

def run_signal_detection(df):
    print("\n" + "="*50)
    print("SIGNAL DETECTION")
    print("="*50)


    print("\n--- Drugs Most Linked to Hospitalization ---")
    df.filter(F.col("outcome") == "Hospitalized") \
      .groupBy("drug_name") \
      .count() \
      .withColumnRenamed("count", "hospitalization_count") \
      .orderBy("hospitalization_count", ascending=False) \
      .show()

    print("\n--- Drugs Most Linked to Death ---")
    df.filter(F.col("outcome") == "Death") \
      .groupBy("drug_name") \
      .count() \
      .withColumnRenamed("count", "death_count") \
      .orderBy("death_count", ascending=False) \
      .show()

    print("\n--- Top Drug–Event Associations ---")
    df.groupBy("drug_name", "adverse_event") \
      .agg(
          F.count("*").alias("occurrences"),
          F.avg("seriousness_score").alias("avg_score")
      ) \
      .orderBy("occurrences", ascending=False) \
      .show(20)