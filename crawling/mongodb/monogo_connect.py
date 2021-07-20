from pymongo import MongoClient
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.util import get_config


data = get_config()
client = MongoClient(data['MONGODB']['url'],data['MONGODB']['port'])

