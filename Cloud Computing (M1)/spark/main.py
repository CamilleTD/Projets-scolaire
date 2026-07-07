from pyspark.sql import SparkSession
from drug_analysis import run_drug_analysis
from event_analysis import run_event_analysis
from temporal_analysis import run_temporal_analysis
from risk_score import run_risk_score
from signal_detection import run_signal_detection
from store_results import store_to_mongo


spark = SparkSession.builder \
    .appName("DrugSafetyAnalytics") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")


DATA_PATH = "/opt/spark-app/data/adverse_events.csv"

df = spark.read.csv(DATA_PATH, header=True, inferSchema=True)
df.cache()

print("\n=== DATASET LOADED ===")
print(f"Total reports: {df.count()}")
df.printSchema()


run_drug_analysis(df)
run_event_analysis(df)
run_temporal_analysis(df)
run_risk_score(df)
run_signal_detection(df)


store_to_mongo(spark, df)

spark.stop()