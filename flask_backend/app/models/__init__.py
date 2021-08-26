import pymongo
from config import Config

class MongoDB:
    conn = pymongo.MongoClient(Config.MONGODB['url'])
    db = conn.test

    @classmethod
    def get_databases(cls):
        return cls.db