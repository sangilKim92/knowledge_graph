const { gql} = require('apollo-server')
const ctrs = require('../../controllers/neo4j')
const { GraphQLJSON, GraphQLJSONObject } = require('graphql-type-json');

const typeDefs = `
scalar JSONObject
scalar JSON
type neo4j {
    result: JSONObject!
}
`

const resolvers = {
    Query:{
        JSONObject : GraphQLJSONObject,
        neo4j : async (parent, args, context) => {
            try{ 
                result = await ctrs.neo4j_read(parent, args, context) 
                return result
            }catch(err){
                console.log(err)
            }
        }
    }
}

module.exports = {
    typeDefs:typeDefs,
    resolvers:resolvers
}