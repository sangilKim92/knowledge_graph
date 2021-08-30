const { gql} = require('apollo-server')
const ctrs = require('../../controllers/person')

const typeDefs = gql`
type movie {
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