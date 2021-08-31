const cors = require('cors')
const express = require('express')
const morgan = require('morgan')
const helmet = require('helmet')
const compression = require('compression')
const auth = require('./auth')
const config = require('./config')
const es = require('../elastic')
const neo4j_error = require('../errors/neo4j-error-handler')

port = process.env.PORT || 5000

const session = {
    secret : process.env.SESSION_SECRET,
    cookie : {},
    resave : false
}
module.exports = function(app,type){
    if (type==="production")
    {
        console.log(`${tpye} mode`)
        session.cookie.secure = true;
        app.use(helmet({contentSecurityPolicy:undefined}))
        app.use(morgan('common'))
    } 
    else
    {
        console.log(`${type} mode`)
        app.use(helmet({contentSecurityPolicy:false}))
        app.use(morgan('dev'))
    }

    // app.use('/graphql',neo4j_error)
    // app.use('/graphql',(req,res,next)=>{
    //     es.ping({
    //         requestTimeout:30000,
    //     }).then( (data) => {
    //         res.send(data);
    //     }).catch(next);
    // })

    app.use(express.json())
    app.use(compression())
    app.use(cors(config.corsOptions))
    app.use(auth)

    app.set('port',port)
}