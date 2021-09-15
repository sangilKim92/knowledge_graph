const { gql } = require('apollo-server')
const ctrs = require('../../controllers/es')
const MyError = require('../../errors/error')

const typeDefs = `
    type es{
        review:String!
        score:Int!
    }
`

const resolvers = {
    Query:{
        elastic : async (parent, args, context) => {
        try{
            return await ctrs.es(parent, args, context)
        }catch(err){
            console.log('Error 발생!')
            return new MyError(err)
            }
        }
    }
}

module.exports = {
    typeDefs:typeDefs,
    resolvers:resolvers
}