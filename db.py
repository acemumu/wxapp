# -*- coding: utf-8 -*-
from flask import g, current_app
from pymongo import MongoClient
import consts
import private_consts

def _test_db_():
    client = MongoClient(consts.DB_IP, consts.DB_PORT)
    db = client.get_database(consts.DB_NAME)
    db.authenticate(private_consts.DB_USER, private_consts.DB_PWD)
    col = db.get_collection('test')
    d = col.find_one({})
    col2 = db.get_collection(consts.COL_OP_INFO)
    col2.insert_one({'b':2})
    client.close()


def get_db():
    if 'db' in g:
        return g.db
    client = MongoClient(consts.DB_IP, consts.DB_PORT)
    db = client.get_database(consts.DB_NAME)
    db.authenticate(private_consts.DB_USER, private_consts.DB_PWD)
    g.db_client = client
    g.db = db
    return db

def get_op_info_collection():
    db = get_db()
    op_info = db.get_collection(consts.COL_OP_INFO)
    return op_info

def close_db():
    client = g.pop('db_client', None)
    g.pop('db', None)
    client and client.close()

if __name__ == '__main__':
    _test_db_()