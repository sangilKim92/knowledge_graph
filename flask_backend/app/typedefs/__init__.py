from ariadne import make_executable_schema, ObjectType, QueryType
from ._query import query_type_defs
from ._mutations import mutation_type_defs, mutation
from .person import person_type_defs, person_resolvers, people_resolvers
from .elastic import elasitc_type_defs, elastic_resolvers
from .neo4j import neo4j_resolvers, neo4j_type_defs
from ._input import input_type_defs
from .mongodb import mongodb_type_defs, mongodb_resolvers

def create_schema():
    type_defs = query_type_defs + \
                mutation_type_defs + \
                input_type_defs + \
                person_type_defs + \
                elasitc_type_defs + \
                neo4j_type_defs + \
                mongodb_type_defs

    query = QueryType()
    query.set_field('person', person_resolvers)
    query.set_field('people', people_resolvers)

    query.set_field('elastic', elastic_resolvers)

    query.set_field('neo4j', neo4j_resolvers)

    query.set_field('mongodb', mongodb_resolvers)

    person = ObjectType("Person")
    elastic = ObjectType("Elastic")
    neo4j = ObjectType("Neo4j")
    mongodb = ObjectType("MongoDB")

    resolvers = [ 
        query,
        mutation,
        person,
        elastic,
        neo4j,
        mongodb
        ]
    schema = make_executable_schema(type_defs, resolvers)
    return schema