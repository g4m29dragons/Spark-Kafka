from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count
import matplotlib.pyplot as plt

# Crear sesión Spark
spark = SparkSession.builder \
    .appName("BatchVentasAnalysis") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# ✅ 1. Cargar dataset
df = spark.read.csv("/home/dasferty/train.csv", header=True, inferSchema=True)

print("=== ESTRUCTURA ===")
df.printSchema()

print("=== DATOS ===")
df.show(5)

# ✅ 2. Limpieza
df = df.dropna()
df = df.dropDuplicates()
df = df.withColumn("Sales", col("Sales").cast("double"))

print("=== DATOS LIMPIOS ===")
df.show(5)

# ✅ 3. TRANSFORMACIÓN (🔥 esto te faltaba para la tarea)
df = df.withColumn("Sales_with_tax", col("Sales") * 1.10)

print("=== DATOS TRANSFORMADOS ===")
df.select("Category", "Sales", "Sales_with_tax").show(5)

# ✅ 4. ANÁLISIS (EDA)

# Ventas por categoría
ventas_categoria = df.groupBy("Category") \
    .agg(sum("Sales").alias("total_sales"))

print("=== VENTAS POR CATEGORIA ===")
ventas_categoria.show()

# Promedio por región
ventas_region = df.groupBy("Region") \
    .agg(avg("Sales").alias("avg_sales"))

print("=== PROMEDIO POR REGION ===")
ventas_region.show()

# Conteo por categoría (🔥 más EDA)
conteo_categoria = df.groupBy("Category") \
    .agg(count("*").alias("total_registros"))

print("=== CONTEO POR CATEGORIA ===")
conteo_categoria.show()

# Top productos
top_productos = df.groupBy("Product Name") \
    .agg(sum("Sales").alias("total_sales")) \
    .orderBy(col("total_sales").desc()) \
    .limit(5)

print("=== TOP PRODUCTOS ===")
top_productos.show()

# ✅ 5. Visualización

pdf = ventas_categoria.toPandas()

plt.figure()
plt.bar(pdf["Category"], pdf["total_sales"])
plt.title("Ventas por Categoría")
plt.xlabel("Categoría")
plt.ylabel("Total Ventas")
plt.savefig("ventas_categoria.png")

print("Gráfica guardada como ventas_categoria.png")

# Finalizar
spark.stop()
