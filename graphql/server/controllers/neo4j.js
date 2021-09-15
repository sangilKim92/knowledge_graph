const client = require('../utils/neo4j')

const neo4j_read = async (parent, args, context) =>{
        try
        {
            const rs = await client.read(args.cypher)
            let result = []
            for( key in rs['records'] ){
                result.push({'result':rs['records'][key]['_fields'][0]})
            }
            return result
        }
        catch(err)
        {
            console.log('에러발생',err)
            return err
        }
}


module.exports = {
    neo4j_read:neo4j_read
}