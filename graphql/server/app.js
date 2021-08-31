const dotenv = require('dotenv')
dotenv.config()

const express = require('express')
const apollo = require('./typedefs-resolvers')
const path = require('path')
const db_setting = require('./models')
const config = require('./utils/config')
const middleware = require('./utils/middleware')
const es = require('./elastic')
const neo4j = require('./utils/neo4j')

root_path = path.resolve(__dirname);

const app = express()

mode = process.env.NODE_ENV || config.node_env

middleware(app,mode)

async function server_setting(){
    try{
        await appPromise(app)
        await new Promise(resolve => app.listen(app.get('port'), resolve));
        console.log(`🚀 Server ready at ${config.app_url}`)

    }catch(err){
        console.log(err)
    }
}

function appPromise(app){
    return Promise.all([apollo.server_setting(app), db_setting()])
}

server_setting()