# SparkProject
As a part of ml for big Data study

### For analyzing fake reviews in amazon




# Requirements:
kafka 2.3.1
scala 2.12
spark

```shell
kafka-topics.sh --zookeeper localhost:2181 \
  --create \
  --topic reviews \
  --partitions 2 \
  --replication-factor 1

kafka-topics.sh --zookeeper localhost:2181 \
  --list \
  --topic reviews 

kafka-topics.sh --zookeeper localhost:2181 \
  --describe \
  --topic reviews
  
  tail_logs.sh | kafka-console-producer.sh \
  --broker-list localhost:9092 \
  --topic retail
  
  ##Validate by consuming messages from the Kafka Topic.
  
  kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic reviews
  
  
  nohup \
  connect-standalone.sh \
  connect-standalone.properties \
  connect-file-source.properties \
  &
  
  
  kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic reviews
  
  
```


# architecture

![Image of ARCH](https://github.com/mcsoverlavdan/SparkProject/blob/master/sprints_details/Untitled%20Diagram.png)


## reviewgenerator py file
Run start_logs.sh to start generating web logs
Run tail_logs.sh to preview while logs are being generated (Hit ctrl-c to come out)
Run stop_logs.sh to stop generating web logs

### new steps to be followed

change the ip address 

```
vim /opt/kafka/config/server.properties
```


to start zookeeper

```
zookeeper-server-start.sh \
  -daemon /opt/kafka/config/zookeeper.properties
```
kafka start 
```
kafka-server-start.sh \
  -daemon /opt/kafka/config/server.properties
```

to create kafka topic

```
kafka-topics.sh --zookeeper localhost:2181 \
  --create \
  --topic retail \
  --partitions 2 \
  --replication-factor 1

kafka-topics.sh --zookeeper localhost:2181 \
  --list \
  --topic retail 

kafka-topics.sh --zookeeper localhost:2181 \
  --describe \
  --topic retail
```

```
tail_logs.sh | kafka-console-producer.sh \
  --broker-list localhost:9092 \
  --topic retail
 ```
 
 optional to validate 
 ```
 kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic retail
 ```
  
 to connect kafka 
 
 ```
 nohup \
  connect-standalone.sh \
  connect-standalone.properties \
  connect-file-source.properties \
  &
 ```

Make sure to validate by consuming messages from the Kafka Topic.
```
kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --topic retail
 
 ```

```
pyspark --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2
```
# References :
https://discuss.itversity.com/t/building-streaming-pipelines-databricks/20087
https://github.com/dgadiraju/gen-logs-python3

