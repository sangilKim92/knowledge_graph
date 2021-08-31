const { ApolloServer } = require('apollo-server')
const { inferSchema, makeAugmentedSchema } = require("neo4j-graphql-js")
const depthLimit = require('graphql-depth-limit')
const config = require('../../utils/config')
const typeDefs = require('./graphql-schema')
const { buildFederatedSchema } = require("@apollo/federation")
const fs = require('fs')

 
async function server_setting(driver){
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

  await neo4j_server.listen({ port: config.neo4j_url.port})
  console.log(`🚀 Neo4j ready at ${config.neo4j_url.url}`)
}

function make_schema(driver){
  return new Promise((resolve, reject)=>{

    inferSchema(driver).then((result) =>{
      fs.writeFile(config.neo4j.schema_url, result.typeDefs, function(err){
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
