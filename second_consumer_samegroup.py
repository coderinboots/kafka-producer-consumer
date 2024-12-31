from kafka import KafkaConsumer

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('topic03',group_id='my-group',
                         bootstrap_servers=['192.168.1.28:9092'], auto_offset_reset='earliest')

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print("%s:%d:%d: key=%s value=%s, type=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value, type(message.value)))

