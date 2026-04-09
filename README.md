# Spark-Kafka
En este repositorio estarán los pasos para colocar a funcionar estas dos aplicaciones en conjunto para poder realizar el análisis de datos de forma facil y grafica.

# Procesamiento de Datos con Apache Spark y Kafka
Se debe hacer uso de la máquina virtual configurada con hadoop y spark trabajada en las actividades anteriores.

## 📌 Descripción
Este proyecto implementa procesamiento de datos en batch usando Apache Spark y procesamiento en tiempo real usando Apache Kafka.

## ⚙️ Tecnologías
- Python
- Apache Spark
- Apache Kafka
- Matplotlib
- putty

### 1. Instalacion
<img width="804" height="673" alt="image" src="https://github.com/user-attachments/assets/96acd480-e19e-4041-8298-3cc266be08ef" />
- Ejecutamos Putty para conectarnos por SSH a la máquina virtual utilizando la IP local
- <img width="449" height="444" alt="image" src="https://github.com/user-attachments/assets/8fa9a469-c388-41a9-a21d-c8476f088ac1" />
- Y nos logueamos nuevamente con el usuario y la contraseña que hallan ingresado al servidor.
- Instalamos mediante PIP la librería de Python Kafka con: pip install kafka-python
- <img width="663" height="217" alt="image" src="https://github.com/user-attachments/assets/fc52b5ba-beb4-42e6-9fe0-662910659edc" />
- Descargue, descomprima y mueva de carpeta Apache Kafka: wget https://downloads.apache.org/kafka/3.9.2/kafka_2.12-3.9.2.tgz
- <img width="713" height="422" alt="image" src="https://github.com/user-attachments/assets/c51b261c-58e5-41f9-9093-32dd698a682e" />
- tar -xzf kafka_2.12-3.8.0.tgz
- sudo mv kafka_2.12-3.8.0 /opt/Kafka

### 2. Iniciamos el servidor ZooKeeper:
sudo /opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties &

Después de un momento y terminada la ejecución del comando anterior se debe dar Enter para que aparezca nuevamente el prompt del sistema

### 3. Iniciamos el servidor Kafka:
sudo /opt/Kafka/bin/kafka-server-start.sh /opt/Kafka/config/server.properties &

Después de un momento y terminada la ejecución del comando anterior se debe dar Enter para que aparezca nuevamente el prompt del sistema
<img width="825" height="445" alt="image" src="https://github.com/user-attachments/assets/dac11d04-2cbc-4444-a4b4-5e0148e147bb" />

### 4. Creamos un tema (topic) de Kafka, el tema se llamará sensor_data
/opt/Kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic sensor_data

### 5. Implementación del productor(producer) de Kafka
- Creamos un archivo llamado kafka_producer.py
nano kafka_producer.py

### 6. Implementación del consumidor con Spark Streaming
- Ahora, crearemos un consumidor(consumer) utilizando Spark Streaming para procesar los datos en tiempo real. Crea un archivo llamado spark_streaming_consumer.py
nano spark_streaming_consumer.py

### 7. Ejecución y análisis
- En una terminal, ejecutamos el productor(producer) de Kafka:
python3 kafka_producer.py

### 8. En otra terminal, ejecutamos el consumidor de Spark Streaming:
- Ejecutamos otra terminal de Putty para conectarnos por SSH a la máquina virtual utilizando la IP local sin cerrar la otra terminal de Putty
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3 spark_streaming_consumer.py


NOTA: es importante primero ejecutar el script de productor y luego el del consumidor
Podemos ver información sobre los Jobs, Stages, entre otros, realizados por Spark, para esto ingresamos a la consola web
http://your-server-ip:4040
Para este caso http://192.168.1.7:4040


## 📊 Resultados
Se obtienen métricas como:
- Promedios
- Sumas
- Visualización de datos

## 👨‍💻 Autor
Jesus Augusto Chacon
