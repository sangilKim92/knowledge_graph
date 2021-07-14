from kafka.producer import KafkaProducer
from json import dumps 
import time 

kafka_topic = "Sang_crawl"

def connect_kafka_producer():
    producer = None
    
    try:
        producer = KafkaProducer(acks=0, compression_type='gzip', 
                                 bootstrap_servers=['localhost:9092'], 
                                 api_version=(0,10))
        
    except Exception as ex:
        print("Error: ", ex)
        
    return producer

def send_to_consumer(object):
    producer = connect_kafka_producer()
    producer.send( kafka_topic ,object.encode('utf-8') )
    producer.flush()