from ariadne import gql, ObjectType, QueryType
from ariadne.asgi import GraphQLSchema
import json
from app.elastic import Elastic

elasitc_type_defs = gql("""
    type Elastic{
        review: String!
        name: String!
        id: ID!
    }
""")


def elastic_resolvers(_, info, _review):
    es = Elastic.elastic_connect()
    body = {
        "query":{
            "match":{
                "review": _review
            }
        }
    }
    res = es.search(index="my-index-restaurant", doc_type="_doc", body=body)
    if res['hits']['total']['value'] > 0:
        result = []
        for item in res['hits']['hits']:
            result.append(item['_source'])
        return result
    else:
        return [{"data": None}]

