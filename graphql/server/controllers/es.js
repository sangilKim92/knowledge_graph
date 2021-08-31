const client = require('../elastic')

const es = async (parent, args, context) =>{
        try
        {
            console.log(args.review)
            const rs = await client.search({
                index: 'my-index-restaurant',
                q: `review:${args.review}`
            })
            result = []
            console.log(rs['hits']['hits'])
            for(var pos = 0; pos < rs['hits']['hits'].length; pos++){
                result.push(rs['hits']['hits'][pos]['_source'])
            }
            console.log(result)
            return result

        }
        catch(err)
        {
            return (err)
        }
}


module.exports = {
    es:es
}