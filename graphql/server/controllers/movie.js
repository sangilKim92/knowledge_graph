const driver = require('../neo4j')
const cypher = require('../neo4j/cypher')

const movie = (parent, args, context) =>{
    return new Promise((resolve, reject)=>{
        try
        {
            const rs = await driver.read(cypher.movieCypher, {$name:args.name})
            console.log(rs)
            resolve(rs)
        }
        catch(err)
        {
            reject(err)
        }
    })
}

const movies = ( parent, args, context ) => {
    return new Promise((resolve, reject)=>{
        try
        {
            const rs = await driver.read(cypher.moviesCypher)
            console.log(rs)
            resolve(rs)
        }
        catch(err)
        {
            reject(err)
        }
    })
}

module.exports = {
    movie:movie,
    movies:movies
}