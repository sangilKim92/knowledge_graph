from ariadne import gql, ObjectType, QueryType
from ariadne.asgi import GraphQLSchema
import json
from app.neo4j import Neo4j

neo4j_type_defs = gql("""
    type Neo4j{
        name: String!
        uuid: ID!
        business: String!
    }
""")


def neo4j_resolvers(_, info):
    query = """MATCH (n) RETURN n LIMIT 25"""
    result = Neo4j.neo4j_query(query, mode = 'read')
    return result