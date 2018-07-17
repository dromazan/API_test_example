import json
from db.db_config import db_path


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
