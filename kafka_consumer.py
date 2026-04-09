from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, window
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
import logging

spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Definir esquema
schema = StructType([
    StructField("Order ID", StringType()),
    StructField("Category", StringType()),
    StructField("Sales", DoubleType()),
    StructField("Region", StringType())
])

# Leer stream desde Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sensor_data") \
    .load()

# Parsear JSON
parsed_df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# Analizar en ventanas de 1 minuto
windowed_stats = parsed_df.groupBy(window(col("Sales"), "1 minute"), "Category").sum("Sales")

# Mostrar en consola
query = windowed_stats.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
