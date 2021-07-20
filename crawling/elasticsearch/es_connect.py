import time, json, sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.util import get_config
from elasticsearch import Elasticsearch
import datetime

data = get_config()
es = Elasticsearch(data['ELASTICSEARCH']['url'])

