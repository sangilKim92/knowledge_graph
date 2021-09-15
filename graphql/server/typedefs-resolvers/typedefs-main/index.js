const { ApolloServer, gql } = require('apollo-server')
const depthLimit = require('graphql-depth-limit')
const _ = require('lodash')
const deepmerge = require('deepmerge')

const config = require('../../utils/config')
const person = require('./person')
const query = require('./_query')
const mutations = require('./_mutations')
const neo4j = require('./neo4j')
const movie = require('./movie')
const es = require('./es')
const { buildFederatedSchema } = require('@apollo/federation')
const { neo4j_read } = require('../../controllers/neo4j')

const typeDefs = gql(`${query}` + 
                     `${mutations}` + 
                     `${person.typeDefs}` + 
                     `${movie.typeDefs}` +
                     `${es.typeDefs}` +
                     `${neo4j.typeDefs}`)

let obj = [ 
          person.resolvers ,
          movie.resolvers ,
          es.resolvers ,
          neo4j.resolvers
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

  await elastic_server.listen({ port: config.main_url.port})
  console.log(`🚀 Main ready at ${config.main_url.url}`)
}

module.exports = {
  server_setting:server_setting
}
