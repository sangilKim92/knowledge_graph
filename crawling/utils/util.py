import json
from collections import namedtuple

def get_config():
    with open('../config.json', 'r' ) as f:
        return (json.loads(f.read()))