const { checkForResolveTypeResolver } = require('graphql-tools');
const mongoose = require('mongoose')
const config = require('../utils/config')


const db_config = function db(){
    return new Promise((resolve,reject)=>{
        mongoose.set('useCreateIndex', true);
        mongoose.connect(config.mongodb.dbServer,{
            dbName: config.mongodb.dbName,
            user: config.mongodb.user,
            pass: config.mongodb.pwd,
            useNewUrlParser: true
            })
            console.log('db connected!')
            
            resolve()
    })
}
module.exports = db_config