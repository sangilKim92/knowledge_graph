const es =  require('elasticsearch')
const config = require('../utils/config')

var client = new es.Client({
    hosts:[
        'http://localhost:9200'
    ]
});

module.exports = client