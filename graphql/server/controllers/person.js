const driver = require('../utils/neo4j')

const person = (parent, args, context) =>{
    return new Promise(async (resolve, reject)=>{
        try{
            resolve(null)
        }catch(err){
            reject(err)
        }
    })

}

const people = ( parent, args, context ) => {
    return new Promise(async (resolve, reject) => {
        try{
            resolve(null)
        }catch(err){
            reject(err)
        }
    })

}

module.exports = {
    people:people,
    person:person
}