const { ApolloServer } = require('apollo-server')
const { inferSchema, makeAugmentedSchema } = require("neo4j-graphql-js")
const depthLimit = require('graphql-depth-limit')
const fs = require('fs')

const config = require('../../utils/config')
const typeDefs = require('./graphql-schema')

const { ApolloGateway} = require('@apollo/gateway')
const { buildFederatedSchema } = require("@apollo/federation")
 

function server_setting(driver){
  return new Promise((resolve,reject)=>{
    const schema = makeAugmentedSchema({ typeDefs , config: { isFederated: true }});

    const neo4j_server = new ApolloServer({
      context:{
        driver,
        driverConfig: { database: config.neo4j.database || 'neo4j' },
      },
      schema: buildFederatedSchema([schema]),
      validationRules: [depthLimit(7)],
      introspection: true, 
      playground: true
  })

    neo4j_server.listen({ port: config.neo4j_url.port}).then(({ url })=>{
    console.log(`🚀 Neo4j ready at ${url}`)
  })
  // server.start()
  // server.applyMiddleware({ app,  path: '/graphql', cors : corsOptions})
  resolve()
  })

}

function make_schema(driver){
  return new Promise((resolve, reject)=>{

    inferSchema(driver).then((result) =>{
  
      fs.writeFile('./typedefs-resolvers/typedefs-neo4j/schema.graphql', result.typeDefs, function(err){
        if (err) return console.log(err);
      })
      console.log("make_schema is finished!")
      resolve(result)
    })
  })
}

module.exports = {
  server_setting:server_setting,
  make_schema : make_schema
}
