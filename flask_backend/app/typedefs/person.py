from ariadne import gql, ObjectType, QueryType
from ariadne.asgi import GraphQLSchema
import json

person_type_defs = gql("""
    type Person{
        id: ID!
        name: String!
        age: Int!
    }
""")

def person_resolvers(_,info):
    data = {"id":1, "name":"홍길동","age":23}
    return data

def people_resolvers(_,info):
    return [
        {"id":"1", "name":"홍길동","age":23},
        {"id":"2", "name":"임꺽정","age":45}
    ]

# query{
#   person{
#     name
#     id
#   }
# }