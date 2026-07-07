from pyspark.sql import functions as F

def run_risk_score(df):
    print("\n" + "="*50)
    print("RISK SCORE COMPUTATION")
    print("="*50)

    severity_map = {
        "Mild":     1,
        "Moderate": 2,
        "Severe":   3,
        "Critical": 4
    }

    df = df.withColumn("severity_num",
        F.when(F.col("severity") == "Mild",     1)
         .when(F.col("severity") == "Moderate", 2)
         .when(F.col("severity") == "Severe",   3)
         .when(F.col("severity") == "Critical", 4)
         .otherwise(1)
    )


    risk_df = df.groupBy("drug_name").agg(
        F.count("*").alias("nb_reports"),
        F.avg("seriousness_score").alias("avg_seriousness"),
        F.avg("severity_num").alias("avg_severity_num")
    )

    risk_df = risk_df.withColumn(
        "risk_score",
        F.round(
            F.col("nb_reports") * F.col("avg_seriousness") * F.col("avg_severity_num"),
            2
        )
    )

    print("\n--- Drug Risk Ranking ---")
    risk_df.select("drug_name", "nb_reports", "avg_seriousness", "risk_score") \
           .orderBy("risk_score", ascending=False) \
           .show()