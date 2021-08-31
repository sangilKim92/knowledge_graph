const driver = require('../neo4j')

const movie = (parent, args, context) =>{
    return new Promise((resolve, reject)=>{
        try
        {
            // const rs = await driver.read(cypher.movieCypher, {$name:args.name})
            // console.log(rs)
            resolve(null)
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
            // const rs = await driver.read(cypher.moviesCypher)
            // console.log(rs)
            resolve(null)
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