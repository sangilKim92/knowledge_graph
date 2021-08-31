const apollo_neo4j = require('./typedefs-neo4j')
const apollo_elastic = require('./typedefs-elastic')
const neo4j = require('../utils/neo4j')
const { ApolloGateway } = require('@apollo/gateway')
const { ApolloServer } = require('apollo-server-express')
const config = require('../utils/config')
const waitOn = require('wait-on')

async function server_setting(app){
    
    const driver = await neo4j.connect()
    await apollo_neo4j.make_schema(driver)
    await graphPromise(driver)

    const gateway = await new ApolloGateway({
        serviceList: [
            {name: 'neo4j', url: config.neo4j_url.url },
            {name: 'elastic', url: config.elastic_url.url }
        ],

        __exposeQueryPlanExperimental: false,
    })
    // Start gateway
    const options= { 
        resources: ['tcp:5001','tcp:5002','tcp:5000']
    }
    waitOn(options)
        .then(()=>{
        const server = new ApolloServer({
        gateway,
        subscriptions: false,
        engine: false
    })
    server.start()
    server.applyMiddleware({ app,  path: '/graphql', cors : config.corOptions})
    })

    return;
}

function graphPromise(driver){
    return Promise.all([apollo_neo4j.server_setting(driver), apollo_elastic.server_setting()])
}

module.exports = {
    server_setting:server_setting
}