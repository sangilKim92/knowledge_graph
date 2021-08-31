const { gql} = require('apollo-server')
const ctrs = require('../../controllers/person')


const typeDefs = `
type movie {
    id: ID!
    released:Int!
    tagline:String!
    title:String!   
}
`

const resolvers = {
    Query:{
        movie : async (parent, args, context) =>
        {
            try{   
                await ctrs.movie(parent, args, context)
            }catch(err){
                console.log(er)
            }
        },
        movies : async (parent, args, context) => {
            try{ 
                await ctrs.movies(parent, args, context)
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