const fs= require('fs')
const path = require('path');
const config = require('../../utils/config');

function typeDefs(){
    try{
        const data = fs
        .readFileSync(
            process.env.GRAPHQL_SCHEMA || path.join(__dirname, 'schema.graphql')
        )
        .toString('utf-8')
        const lines = data.split(/\r?\n/);
        return lines.filter(line=>(!line.includes('_id: Long!'))).join('\n')
    }catch(err){
        console.log(err)
    }
  }

module.exports = typeDefs()