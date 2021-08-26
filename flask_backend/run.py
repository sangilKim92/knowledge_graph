import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

if os.path.exists('.env'):
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0].strip()] = var[1].strip()

from config import Config
from app import create_app
from app.models import MongoDB

# if os.environ.get('FLATCOKE') == 'production':
#     app = DispatcherMiddleware(create_app(os.environ.get("MODE")), {
#         '/api': create_app('api')
#     })
# else:
#     app = create_app(os.environ.get("FLATCOKE") or 'development')
app = create_app(os.getenv("MODE") or 'development', Config)

#with app.app_context():

# with app.app_context():
#     close_elasticsearch()

#app.run()
# if __name__ == '__main__':
#    app.run()
db = MongoDB.get_databases()
print(db)
print(db.list_collection_names())