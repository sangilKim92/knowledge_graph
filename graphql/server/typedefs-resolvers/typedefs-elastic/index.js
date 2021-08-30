const { ApolloServer } = require('apollo-server')
const depthLimit = require('graphql-depth-limit')

const config = require('../../utils/config')
const person = require('./person')
const query = require('./_query')
const mutations = require('./_mutations')
const movie = require('./movie')
const { buildFederatedSchema } = require('@apollo/federation')

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

// const schema = buildFederatedSchema([{
//   typeDefs,
//   resolvers
// }])

function server_setting(){
  return new Promise((resolve,reject)=>{
    
    const elastic_server = new ApolloServer({
      // schema: schema,
      typeDefs,
      resolvers,
      validationRules: [depthLimit(7)],
      introspection: true, 
      playground: true
  })

  elastic_server.listen({ port: config.elastic_url.port}).then(({ url })=>{
  console.log(`🚀 ealstic ready at ${url}`
  )
  })

  resolve()
  reject()
})
}

module.exports = {
  server_setting:server_setting
}
