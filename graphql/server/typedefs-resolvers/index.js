const { ApolloServer, gql} = require('apollo-server-express')
const depthLimit = require('graphql-depth-limit')
const person = require('./person')
const query = require('./_query')
const mutations = require('./_mutations')
const movie = require('./movie')

const typeDefs =[
  query,
  mutations,
  person.typeDefs,
  movie.typeDefs
]

const resolvers = [
  person.resolvers,
  movie.resolvers
]


module.exports = function(app,corsOptions){
    return new Promise((resolve,reject)=>{
      const server = new ApolloServer({
        typeDefs,
        resolvers,
        validationRules: [depthLimit(7)],
        introspection: true, 
        playground: true
    })

    server.start()

    server.applyMiddleware({ app,  path: '/graphql', cors : corsOptions})
    console.log('graphql connected!')
    resolve()
    })

}