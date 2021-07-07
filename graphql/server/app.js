const dotenv = require('dotenv')
dotenv.config()

const express = require('express')
const apollo = require('./typedefs-resolvers')
const path = require('path')
const db_setting = require('./models')
const config = require('./utils/config')
const middleware = require('./utils/middleware')
const es = require('./elastic')
const neo4j = require('./neo4j')

root_path = path.resolve(__dirname);

const app = express()

mode = process.env.NODE_ENV || config.node_env

middleware(app,mode)

async function server_setting(){
    try{
        await db_setting()
        await apollo(app,config.corsOptions)
        await new Promise(resolve => app.listen(app.get('port'), resolve));
        console.log(`🚀 Server ready at http://localhost:${app.get('port')}/graphql`)

    }catch(err){
        console.log(err)
    }
}
server_setting()

