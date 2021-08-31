const { gql } = require('apollo-server')
const ctrs = require('../../controllers/es')

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
            console.log("Error: ",err)
            return {"data":null}
        }
        }
    }
}

module.exports = {
    typeDefs:typeDefs,
    resolvers:resolvers
}