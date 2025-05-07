from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.appName("Clean CSV").getOrCreate()

df = spark.read.csv("gs://sreeja-bucket/insert/2_raw_data.csv", header=True, inferSchema=True)

# Drop rows with nulls
df_clean = df.dropna()

# Cast column types
df_clean = df_clean.withColumn("age", df_clean["age"].cast(IntegerType()))

df_clean.write.csv("gs://sreeja-bucket/output/cleaned_data", header=True)

spark.stop()
