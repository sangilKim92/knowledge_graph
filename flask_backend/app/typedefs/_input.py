from ariadne import MutationType, make_executable_schema
from ariadne import gql

input_type_defs = gql("""    
    input PostPersonInput{
        id: String!
        name: String!
        age: Int!
    }
""")
