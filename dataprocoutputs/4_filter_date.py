from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, col

spark = SparkSession.builder.appName("Date Filter").getOrCreate()

df = spark.read.csv("gs://sreeja-bucket/input/4_events_csv.csv", header=True, inferSchema=True)

df = df.withColumn("event_date", to_date(col("event_date"), "yyyy-MM-dd"))

# Filter for March 2024
march_df = df.filter((col("event_date") >= "2024-03-01") & (col("event_date") <= "2024-03-31"))

march_df.write.csv("gs://sreeja-bucket/output/march_events", header=True)

spark.stop()
