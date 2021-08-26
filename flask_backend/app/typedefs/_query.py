from ariadne import gql, ObjectType, QueryType
from ariadne.asgi import GraphQLSchema

query_type_defs = gql("""
    type Query{
        person: Person
        people: [Person]  
        elastic(_review:String!): [Elastic]
        neo4j: [Neo4j]
        mongodb: [MongoDB]
    }
""")