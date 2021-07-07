const driver = require('../neo4j')
const cypher = require('../neo4j/cypher')

const person = (parent, args, context) =>{
    return new Promise(async (resolve, reject)=>{
        try{
            console.log(new Date());
            const rs = await driver.read(cypher.personCypher, {"name":args.name})
            console.log(new Date());
            resolve(rs)
        }catch(err){
            reject(err)
        }
    })

}

const people = ( parent, args, context ) => {
    return new Promise(async (resolve, reject) => {
        try{
            console.log(new Date());
            const rs = await driver.read(cypher.peopleCypher)
            var jsonArray = new Array();
            rs['records'].map( (item) => jsonArray.push(item._fields[0]['properties']))
            console.log(new Date());
            resolve(jsonArray)
        }catch(err){
            reject(err)
        }
    })

}

module.exports = {
    people:people,
    person:person
}