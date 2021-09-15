const fs= require('fs')
const path = require('path');
const config = require('../../utils/config');

function typeDefs(){
    try{
        const data = fs
        .readFileSync(
            config.neo4j.schema_url || path.join(__dirname, 'schema.graphql')
        )
        .toString('utf-8')
        const lines = data.split(/\r?\n/).filter( line => ( !line.includes('_id: Long!') ) ).join('\n')
        
        const data2 = fs.readFileSync(
            '/home/com/github/graphql/server/typedefs-resolvers/typedefs-neo4j/custom.graphql'
        )
        .toString('utf-8')
        
        return lines + data2
    }catch(err){
        console.log(err)
    }
}

module.exports = typeDefs()