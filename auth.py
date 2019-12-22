# -*- coding: utf-8 -*-

import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
import time
import consts
import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        pass
    return render_template('auth/register.html')


@auth_bp.route('/login', methods=('GET', 'POST'))
def login():
    # if not request.args or 'oid' not in request.args:
    #     return 'invalid args'
    #
    # open_id = request.args['oid']
    # if not CheckValidOpenId(open_id):
    #     return '关注公众号后，回复：%s' % consts.REGISTER_OP_INFO

    if request.method == 'POST':
        user_name = request.form['name']
        phone = request.form['phone']
        date = request.form['op_date']
        data = {
            '_id': open_id,
            'name': user_name,
            'phone': phone,
            'op_date': date
        }
        res = SaveOpInfo(data)
        return '提交成功' if res else '提交失败，请联系后台！'
    else:
        pass
    #

    Data = {
        'Title': consts.REGISTER_OP_INFO,
    }
    return render_template('auth/login3.html', **Data)

def SaveOpInfo(data):
    col_info = db.get_op_info_collection()
    res = col_info.update_one({'phone':data['phone'], 'name': data['name']}, {'$set':data}, upsert=True)
    if res and (res.modified_count or res.upserted_id or res.matched_count):
        return True
    return False


def CheckValidOpenId(open_id):
    col_info = db.get_op_info_collection()
    res = col_info.find_one({'_id':open_id})
    logger.info('-------res:%s', res)
    return not not res