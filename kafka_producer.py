import time
import json
import pandas as pd
from kafka import KafkaProducer

# Cargar dataset
file_path = "/home/dasferty/train.csv"
df = pd.read_csv(file_path)

# Crear productor Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# Enviar fila por fila como mensaje Kafka
for index, row in df.iterrows():
    data = {
        "Order ID": row["Order ID"],
        "Category": row["Category"],
        "Sales": float(row["Sales"]),
        "Region": row["Region"]
    }
    producer.send('sensor_data', value=data)
    print(f"Sent: {data}")
    time.sleep(0.1)  # simulamos llegada de datos en tiempo real
