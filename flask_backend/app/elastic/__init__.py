
from elasticsearch import Elasticsearch
from config import Config

class Elastic:
    es = Elasticsearch(hosts = Config.ES['url'], timeout = 10, http_compress = True)

    @classmethod
    def elastic_search(cls, index, body, doc_type = "_doc" ):
        return cls.es.search(index=index, doc_type = doc_type,body = body)['hits']['hits'][0]['_source']
    
    @classmethod
    def elastic_insert(cls, index, body):
        pass
    
    @classmethod
    def elastic_connect(cls):
        return cls.es