from pyspark.sql import functions as F

def run_event_analysis(df):
    print("\n" + "="*50)
    print("ADVERSE EVENT ANALYSIS")
    print("="*50)

    print("\n--- Most Frequent Adverse Events ---")
    df.groupBy("adverse_event") \
      .count() \
      .orderBy("count", ascending=False) \
      .show()

    print("\n--- Most Severe Adverse Events (avg score) ---")
    df.groupBy("adverse_event") \
      .agg(
          F.avg("seriousness_score").alias("avg_seriousness"),
          F.count("*").alias("nb_reports")
      ) \
      .orderBy("avg_seriousness", ascending=False) \
      .show()

    print("\n--- Events by Severity Level ---")
    df.groupBy("severity") \
      .count() \
      .orderBy("count", ascending=False) \
      .show()