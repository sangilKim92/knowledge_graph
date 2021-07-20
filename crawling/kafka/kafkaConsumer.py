from kafka import KafkaConsumer
import time, json, sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.util import get_config

kafka_topic = "crawl"
# topic, broker list

if __name__ == '__main__':
    consumer = KafkaConsumer(
        kafka_topic,
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest', #consume 가장 앞쪽부터
        group_id = 'sang_group',
        api_version=(0,10)
    )
    print(consumer)
    # consumer list를 가져온다
    print('[begin] get consumer list')
    for message in consumer:
        print( "Value: %s" % (
            loads(message.value)
        ))
    print('[end] get consumer list')
