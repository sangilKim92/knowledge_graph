from kafka.producer import KafkaProducer
from json import dumps 
import time, json, sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.util import get_config


kafka_topic = "crawl"

def json_serializer(data):
    return dumps(data).encode('utf-8')

def connect_kafka_producer():
    producer = None
    
    try:
        producer = KafkaProducer(acks=0, compression_type='gzip', 
                                 bootstrap_servers=['localhost:9092'], 
                                 api_version=(0,10),
                                 value_serializer = json_serializer
                                 )
                                         
    except Exception as ex:
        print("Error: ", ex)
        
    return producer


def send_to_consumer(object):
    producer = connect_kafka_producer()
    print(object)
    producer.send( kafka_topic , object)
    producer.flush()