from ariadne import gql, ObjectType, QueryType
from ariadne.asgi import GraphQLSchema
import json
from app.models import MongoDB

mongodb_type_defs = gql("""
    type MongoDB{
        review: String!
        name: String!
        id: ID!
    }
""")


def mongodb_resolvers(_, info):
    db = MongoDB.get_databases()
    result = db.first_collection.find_one()
    print(result)
    return result