# -*- coding: utf-8 -*-


# NOTE: 解决中文编码问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time, traceback
import urllib, urllib2
import wx_api_util
import consts
from pymongo import MongoClient
import private_consts
import json

SLEEP_TIME = 3600

DB_CLIENT = None
DB = None


def con_db():
    global DB_CLIENT, DB

    if DB_CLIENT:
        return
    client = MongoClient(consts.DB_IP, consts.DB_PORT)
    db = client.get_database(consts.DB_NAME)
    db.authenticate(private_consts.DB_USER, private_consts.DB_PWD)
    DB_CLIENT = client
    DB = db

def close_db():
    global DB_CLIENT, DB
    if not DB_CLIENT:
        return
    DB_CLIENT.close()
    DB_CLIENT = None
    DB = None
    print 'db closed'


class PostData(object):
    def __init__(self, touser, first, k_list, remark):
        self.touser = touser
        self.temp_id = private_consts.TEMPLATE_ID
        self.first = first
        self.k_list = k_list
        self.remark = remark

    def Pack(self):
        # 可以添加手机号码
        template = {
            "touser": self.touser,
            "template_id": self.temp_id,
        }
        data = {
            "first": {
                "value": self.first,
                "color": "#173177"
            },
            "remark": {
                "value": self.remark,
                "color": "#173177"
            }
        }
        for idx, kvalue in enumerate(self.k_list):
            data['keyword%s'%(idx+1)] = {
                'value': kvalue,
                "color": "#173177"
            }
        template['data'] = data
        return template

def NotifyMsg():
    col = DB.get_collection(consts.COL_OP_INFO)
    cur = col.find()
    for doc in cur:
        if False:
            # TODO add check date
            continue

        oid = doc['_id']
        name = 'hello' # doc['name']
        first = consts.TEMPLATE_TITLE.format(name=name)
        op_date = doc['op_date']
        check_date = "fucha 2020-12-12"
        remark = 'Thanks'
        temp_data = PostData(oid, first, [name, op_date, check_date], remark)
        post_data = temp_data.Pack()
        print post_data
        # return
        url = consts.TEMPLATE_MSG_POST_URL % private_consts.ACCESS_TOKEN
        print url
        urllib.urlopen(url, data= json.dumps(post_data))
        return
        post_data = urllib.urlencode(post_data)
        print post_data
        opener = urllib2.build_opener()
        res = opener.open(url, data=post_data).read()
        print 'post res:', res
        time.sleep(1)

def Update():
    # while 1:
    wx_api_util.InitOrGetAccessToken()
    con_db()
    NotifyMsg()
    close_db()
    # except Exception, e:
    #     print traceback.extract_stack()
    #     print 'Traceback:', e
    # finally:
    #     close_db()
    # time.sleep(SLEEP_TIME)


if __name__ == '__main__':
    Update()