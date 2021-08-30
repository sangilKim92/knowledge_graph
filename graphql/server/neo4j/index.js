const neo4j = require('neo4j-driver')
const config = require('../utils/config')


function connect(){
    return new Promise((resolve,reject)=>{
        driver = new neo4j.driver(config.neo4j.url, neo4j.auth.basic(config.neo4j.user, config.neo4j.pwd))
        console.log('neo4j is connected!')
        resolve(driver)
    })
    
}
function read(cypher, params = {}, database = config.neo4j.database) {
    const session = driver.session({
        defaultAccessMode: neo4j.session.READ,
        //database,
    })

    return session.run(cypher, params)
        .then(res => {
            session.close()
            return res
        })
        .catch(e => {
            session.close()
            throw e
        })
}

function write (cypher, params = {}, database = config.neo4j.database){
    const session = driver.session({
        defaultAccessMode: neo4j.session.WRITE,
        //database,
    })

    return session.run(cypher, params)
        .then(res => {
            session.close()
            return res
        })
        .catch(e => {
            session.close()
            throw e
        })
}

module.exports = {
    read: read,
    write: write,
    connect: connect
}