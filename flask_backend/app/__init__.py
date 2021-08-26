#from flask import Flask, request
#from flask_restful import Resource, Api
from .typedefs import create_schema
from ariadne.asgi import GraphQL
from .neo4j import Neo4j

def create_app(MODE,CONFIG):
    if MODE == 'production':
        print('production mode!')
    else:
        print('developer mode!')

    app = None
    #app = Flask('sang_app')
    schema = create_schema()
    app = GraphQL(schema, debug=True)
    #app.secret_key = CONFIG.SECRET_KEY

    return app

# class App:
#     def __init__(self, CONFIG):
#         self.config = CONFIG
#         self.app = Flask(__name__)
#         self.app.secret_key = CONFIG.SECRET_KEY
#         self.graphql = GraphQL(schema, debug = True)
#         self.elastic = get_elasticsearch(self.config)
#         self.neo4j = GraphDatabase.driver(uri, auth=(user, password))
