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
    field_def = info.parent_type.fields[info.field_name]
    directive = info.schema.get_directive("example")
    print(info)
    print(info.field_nodes[0].name.value)
    # print(help(info))
    # print(directive)
    # print(info.fragments)
    # print(info.path)
    # print(info.schema)
    # print(info)
    # print(info.field_nodes[0].arguments)
    # print(info.field_nodes[0].name)
    # print(help(info.field_nodes[0]))
    # print(info.field_nodes[0].alias)
    # print(info.field_nodes[0].selection_set)
    # print(info.field_nodes[0].loc)
    # print(info.field_nodes[0].directives)
    # # print(info.field_nodes[0])
    # print(info.field_nodes[0].kind)
    # print(info.field_nodes[0].keys)
    # # print(help(info.operation))
    # print(info.operation.loc)
    # print(info.operation.name)
    # print(info.operation.directives)
    # print(info.operation.variable_definitions)
    # print(info.operation.selection_set)
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