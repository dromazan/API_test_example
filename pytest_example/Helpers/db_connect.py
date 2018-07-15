from flata import Flata, where
from flata.storages import JSONStorage
from pytest_example.Resources.resources import db_path
from jsondb.db import Database


def connect_db():
    db = Flata(db_path, storage=JSONStorage)
    return db