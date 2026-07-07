from pyspark.sql import functions as F

def run_drug_analysis(df):
    print("\n" + "="*50)
    print("DRUG ANALYSIS")
    print("="*50)

    # Top reported drugs
    print("\n--- Top Reported Drugs ---")
    df.groupBy("drug_name") \
      .count() \
      .orderBy("count", ascending=False) \
      .show()

    # Number of reports by drug class
    print("\n--- Reports by Drug Class ---")
    df.groupBy("drug_class") \
      .count() \
      .orderBy("count", ascending=False) \
      .show()

    # Severe reports by drug (Severe + Critical)
    print("\n--- Severe Reports by Drug ---")
    df.filter(F.col("severity").isin(["Severe", "Critical"])) \
      .groupBy("drug_name") \
      .count() \
      .withColumnRenamed("count", "severe_count") \
      .orderBy("severe_count", ascending=False) \
      .show()