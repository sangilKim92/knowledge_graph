const { gql} = require('apollo-server-express')
const driver = require('../neo4j')
const cypher = require('../neo4j/cypher')
const ctrs = require('../controllers/person')

const typeDefs = gql`
type movie{
    id: ID!
    released:Int!
    tagline:String!
    title:String!   
}
`

const resolvers = {
    Query:{
        movie : async (parent, args, context) => ctrs.movie(parent, args, context),
        movies : async (parent, args, context) =>ctrs.movies(parent, args, context)
    }
}

module.exports = {
    typeDefs:typeDefs,
    resolvers:resolvers
}