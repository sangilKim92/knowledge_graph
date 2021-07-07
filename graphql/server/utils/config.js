const config = {
    mongodb:{
    dbServer: process.env.ATLAS_CLOUD,
    dbName: process.env.DB_NAME,
    user: process.env.DB_USER,
    pwd: process.env.DB_PASS
    },
    app_url :'localhost:5000',
    api_url : 'localhost:5000',
    corOptions :{
        origin: '*', // 허락하고자 하는 요청 주소
        credentials: true, // true로 하면 설정한 내용을 response 헤더에 추가 해줍니다        
    },

    es:{
        url:'http://localhost:9200'
    },
    neo4j:{
        url:'bolt://35.175.115.90:7687',
        secret_key: process.env.NEO_SECRET_KEY,
        user : process.env.NEO_USER,
        pwd : process.env.NEO_PWD,
        database: 'Movies'
    },
    node_env : 'developer'
}

module.exports = config