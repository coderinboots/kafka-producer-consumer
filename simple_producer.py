import json
from kafka import KafkaProducer
from kafka.errors import KafkaError
producer = KafkaProducer(bootstrap_servers=['192.168.1.28:9092'])


future = producer.send('topic03', key=b'hello', value=b'This is my 1st message')

try:
    record_metadata = future.get(timeout=10)
    print("topic -->", record_metadata.topic)
    print("partition -->", record_metadata.partition)
    print("offset -->", record_metadata.offset)
except KafkaError as e:
    print("Error while sending message to Kafka ", e)
