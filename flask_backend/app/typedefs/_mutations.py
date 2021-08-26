from ariadne import MutationType, make_executable_schema
from ariadne import gql

mutation_type_defs = gql("""
    type Mutation{
        addPerson(name:String): Person
        postPerson(args:PostPersonInput): Person
    }
""")

mutation = MutationType()

@mutation.field("addPerson")
def addPerson_resolvers(*_, name):
    print(name)
    return {"name":name,"age":123,"id":"test"}
# mutation{
#   addPerson(name:"하하"){
#     name
#     age
#   }
# }

@mutation.field("postPerson")
def postPerson_resolvers(*_, args):
    return {"id":args['id'],"name":args['name'],"age":args['age']}

# mutation{
#   postPerson(args:{name:"김상일"
#   									age:30
#   									id:"123dsgsd"})
#   {
#     name
#   }
# }

