import json
from db.db_config import db_path

# db_path = os.path.abspath('C:\\Users\\dromaz\\PycharmProjects\\API_test_example\\db\\db.json')
# db_path = os.path.dirname(sys.modules['__main__'].__file__) + 'db\\db.json'

def connect_db():
    with open(db_path, "r") as read_file:
        data = json.load(read_file)
    return data


def find_post(db, dict):
    return dict in db.get('posts')


def find_post_by_id(db, id):
    for i in db.get('posts'):
        if i.get('id') == id:
            return i
    return ValueError
