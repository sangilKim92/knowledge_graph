const { gql } = require('apollo-server')
const ctrs = require('../../controllers/es')

typeDefs = gql`
    type es{
        text:String!
        score:Int!
    }
`


const resolvers = {
    Query:{
        es : async (parent, args, context) => ctrs.movie(parent, args, context)
    }
}

module.exports = {
    typeDefs:typeDefs,
    resolvers:resolvers
}