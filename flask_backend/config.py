import os

BASE_DIL = os.path.abspath(os.path.dirname(__file__))

class Config:
    MONGODB = {
        'url' : "mongodb://localhost:27017",
        'name' : "test",
        'user' : os.getenv('DB_USER'),
        'pwd' : os.getenv('DB_PASS')
    }

    APP_URL = 'localhost:5000'
    API_URL = 'localhost:5000'
    
    corOptions = {
        'origin': '*',
        'creadentials' : True
    }

    ES = {
        'url' : 'http://localhost:9200',
        'options': None
    }
    
    NEO4j = {
        'url' : 'bolt://127.0.0.1:7687',
        'secret_key' : os.getenv('NEO_SECRET_KEY'),
        'user' : os.getenv('NEO_USER'),
        'pwd' : os.getenv('NEO_PWD'),
        'database' : 'Movies'
    }

    SECRET_KEY = os.getenv('SECRET_KEY')