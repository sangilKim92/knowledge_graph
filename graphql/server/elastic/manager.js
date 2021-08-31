const config = require('../utils/config')
const es = require('./index')
const constants = require('../utils/constant')
const bodybuilder = require('bodybuilder');
const oError = require('../errors/error')

function manger(ES_METHOD){
    switch(ES_METHOD){
        case constants.ELASTIC_SEARCH:
            return 0;
        case constants.ES_NUM.PUT:
            return;
        case constants.ES_NUM.DELETE:
            return ;
        case constants.ES_NUM.UPDATE:
            return;
        case constants.ES_NUM.MAPPING:
            return;
    }
}

function search(req,res, next){
    const { query } = req.body;
    let body = bodybuilder();
    let searchText;

    if(!query.serchtext){
        res.status(oError.NO_ELASTICSEARCH_QUERY.status_code)
        return res.send(oError.NO_ELASTICSEARCH_QUERY.message)
    }
    
}
const search = async function search(body){
    try
    {
        const rs = await es.search({
        
            index: body.index,
            from: body.from,
            size: body.size,
            body:
            {
                query:
                {
                    movideCd:"1"
                }
            }
        },{
            ignore:[404],
            maxRetries:3
        })
    }
    catch(err){
        console.log(err)
    }
}
const createIndex = async function create(){
    try{
        const rs = await es.indices.create({
            index:'test2'
        })

        console.log('create: ',rs)
    }catch(err){
        console.log(err)
    }
}

const deleteIndex = async function deleteIndex(){
    try
    {
        const rs = await es.indices.delete({
            index:'test2'
        })
        
        console.log('remove: ',rs)
    }
    catch(err)
    {
        console.log(err)
    }
}

const createDoc = async function (){
    try
    {
        const rs = await es.index({
            index:'test2',
            id: '1',
            type:'constituencies',
            body:{
                "name":"sangil",
                "age":30
            }
        })
    }
    catch(err)
    {
        console.log(err)
    }
}
module.exports = {
    search:search,
    createIndex:createIndex,
    createDoc: createDoc,
    deleteIndex: deleteIndex
}