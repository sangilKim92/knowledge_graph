from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
from config import Config

class Neo4j:
    driver = GraphDatabase.driver(uri=Config.NEO4j['url'], auth=(Config.NEO4j['user'], Config.NEO4j['pwd']), encrypted = False)

    @classmethod
    def neo4j_connect(cls):
        return cls.driver

    @classmethod
    def neo4j_query(cls, query, mode = 'read', data = None):
        if not query:
            return None

        if mode == 'read':
            with cls.driver.session() as session:
                return session.read_transaction(cls.neo4j_cypher, query, data)
        elif mode == 'write':
            with cls.driver.session() as session:
                return sessin.write_transaction(cls.neo4j_cypher, query, data)
    
    @classmethod
    def neo4j_cypher(cls, tx, cypher, data = None):
        result = []
        for item in (tx.run(cypher)):
            value = {}
            for key in item['n']:
                value[key] = item['n'][key]
            result.append(value)
        return result