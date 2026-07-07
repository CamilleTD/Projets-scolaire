from pyspark.sql import functions as F

def run_temporal_analysis(df):
    print("\n" + "="*50)
    print("TEMPORAL ANALYSIS")
    print("="*50)

    df = df.withColumn("report_date", F.to_date("report_date", "yyyy-MM-dd"))
    df = df.withColumn("year",  F.year("report_date"))
    df = df.withColumn("month", F.month("report_date"))


    print("\n--- Monthly Evolution of Reports ---")
    df.groupBy("year", "month") \
      .count() \
      .orderBy("year", "month") \
      .show()

    print("\n--- Monthly Evolution of Severe Cases ---")
    df.filter(F.col("severity").isin(["Severe", "Critical"])) \
      .groupBy("year", "month") \
      .count() \
      .withColumnRenamed("count", "severe_count") \
      .orderBy("year", "month") \
      .show()