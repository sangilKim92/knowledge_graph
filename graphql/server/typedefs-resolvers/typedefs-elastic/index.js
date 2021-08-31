const { ApolloServer, gql } = require('apollo-server')
const depthLimit = require('graphql-depth-limit')
const _ = require('lodash')
const deepmerge = require('deepmerge')

const config = require('../../utils/config')
const person = require('./person')
const query = require('./_query')
const mutations = require('./_mutations')
const movie = require('./movie')
const es = require('./es')
const { buildFederatedSchema } = require('@apollo/federation')

const typeDefs = gql(`${query}` + 
                     `${mutations}` + 
                     `${person.typeDefs}` + 
                     `${movie.typeDefs}` +
                     `${es.typeDefs}`)

let obj = [ 
          person.resolvers ,
          movie.resolvers ,
          es.resolvers 
          ]


async function server_setting(){
  let resolvers = null

  for (var pos = 0; pos < obj.length -1; pos++){
    if (resolvers == null){
      resolvers = obj[pos]
    }
    resolvers = deepmerge(resolvers,obj[pos+1])
  }

  const schema = buildFederatedSchema([{typeDefs, resolvers}])

  const elastic_server = new ApolloServer({
    schema: schema,
    validationRules: [depthLimit(7)],
    introspection: true, 
    playground: true
  })

  await elastic_server.listen({ port: config.elastic_url.port})
  console.log(`🚀 elastic ready at ${config.elastic_url.url}`)
}

module.exports = {
  server_setting:server_setting
}
