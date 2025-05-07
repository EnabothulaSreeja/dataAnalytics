from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark SQL on Dataproc") \
    .getOrCreate()

# Replace with your GCS path
df = spark.read.csv("gs://sreeja-bucket/input/sales_data.csv", header=True, inferSchema=True)

df.createOrReplaceTempView("sales_data")


# Select specific columns
selected_columns = spark.sql("SELECT product_name, price FROM sales_data")
selected_columns.write.csv("gs://sreeja-bucket/output/selected_columns.csv", header=True, mode="overwrite")



# Filter rows
result_high_sales = spark.sql("SELECT * FROM sales_data WHERE amount > 500")
result_high_sales.write.csv("gs://sreeja-bucket/output/high_value_sales.csv", header=True, mode="overwrite")

# Count
sales_count = spark.sql("SELECT COUNT(*) as total_rows FROM sales_data")
sales_count.write.csv("gs://sreeja-bucket/output/sales_count.csv", header=True, mode="overwrite")


# Group and aggregate
groupby_result = spark.sql("SELECT product_name,"
           "COUNT(*) as count," 
           "SUM(qty) as total_sales," 
           "AVG(qty) as average_sales"
    " FROM sales_data"
    " GROUP BY product_name")
groupby_result.write.csv("gs://sreeja-bucket/output/groupby_result.csv", header=True, mode="overwrite")











