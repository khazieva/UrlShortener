import os
from sqlitedict import SqliteDict


def init_db(base_path):
    mydict = SqliteDict(base_path, autocommit=True)
    return mydict


def remove_db(base_path):
    os.remove(base_path)
