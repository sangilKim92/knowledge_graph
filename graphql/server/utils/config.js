const config = {
    mongodb:{
    dbServer: process.env.ATLAS_CLOUD,
    dbName: process.env.DB_NAME,
    user: process.env.DB_USER,
    pwd: process.env.DB_PASS
    },

    neo4j_url :{
        url:'http://localhost:5001/graphql',
        port: 5001,
        path: 'graphql'

    },
    elastic_url:{
        url:'http://localhost:5002/graphql',
        port: 5002,
        path: 'graphql'
    },
    app_url : 'http://localhost:5000/graphql',
    api_url : 'localhost:5000',

    corOptions :{
        origin: '*', // 허락하고자 하는 요청 주소
        credentials: true, // true로 하면 설정한 내용을 response 헤더에 추가 해줍니다        
    },

    es:{
        url:'http://localhost:9200'
    },
    neo4j:{
        url:'bolt://127.0.0.1:7687',
        secret_key: process.env.NEO_SECRET_KEY,
        user : process.env.NEO_USER,
        pwd : process.env.NEO_PWD,
        database: 'neo4j',
        schema_url: process.env.GRAPHQL_SCHEMA
    },
    node_env : 'developer'
}

module.exports = config