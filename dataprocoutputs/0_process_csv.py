from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Demo CSV Processor").getOrCreate()

# Read CSV
df = spark.read.csv("gs://sreeja-bucket/injection/0_input.csv", header=True, inferSchema=True)

# Process: Example - filter and select
filtered_df = df.filter(df["SrNo"] > 3).select("Name", "SrNo")

# Write to output
filtered_df.write.csv("gs://sreeja-bucket/output/processed", header=True)

spark.stop()




