const { gql} = require('apollo-server-express')
const driver = require('../neo4j')
const cypher = require('../neo4j/cypher')
const ctrs = require('../controllers/person')

const typeDefs = gql`
type person{
    id: ID!
    born: Int!
    name: String!
}
`

var aJson = new Object();
var jsonArray = new Array();

const resolvers = {
    Query:{
        people: async (parent, args, context) =>  {
            try{
            const jsonArray = await ctrs.people(parent, args, context)
            return jsonArray
            }catch(err){
                console.log(err)
            }
        },
        person: async (parent, args, context,info) =>  {
            try{
                const rs = await ctrs.person(parent, args, context)
                return rs['records'][0]._fields[0].properties
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