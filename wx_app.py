# -*- coding: utf-8 -*-

from flask import Flask, request
import __builtin__
import logging
from logging.handlers import RotatingFileHandler
import consts
import db
import auth
import __builtin__


import wx_api_util

# NOTE: 解决中文编码问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def AppInit():
    # 日志的等级的设置
    # logging.basicConfig(level=logging.DEBUG)
    # # 创建日志记录器，　指明日志保存的路径、每个日志的大小、保存日志的上限
    # file_log_handler = RotatingFileHandler('/flask_log', maxBytes=1024*1024, backupCount=10)
    # # 设置日志的格式       日志等级       日志信息的文件名　　行数　　日志信息
    # formatter = logging.Formatter('%(levelname)s %(filename)s %(lineno)d %(message)s')
    # # 将日志记录器指定日志的格式
    # file_log_handler.setFormatter(formatter)
    # # 为全局的日志工具对象添加日志记录器
    # logging.getLogger().addHandler(file_log_handler)
    from logging.config import dictConfig
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })
    wx_api_util.InitOrGetAccessToken()


def OnTearDown(*args):
    logging.info('Request App Release:%r' % args)
    db.close_db()

def CreateApp():
    AppInit()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATA_BASE='wxdb',
    )
    try:
        import os
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.teardown_appcontext(OnTearDown)
    app.register_blueprint(auth.auth_bp)

    @app.route('/')
    def hello_world():
        return 'hello world, Flask!'

    @app.route('/wx_login', methods=['GET', 'POST'])
    def wx_login():
        if 'nonce' not in request.args or 'timestamp' not in request.args:
            return 'Invalid args'
        app.logger.info('GET_ARGS: %r, %r', request.args['nonce'], request.args['timestamp'])
        if request.method == 'GET':
            data = request.args
            res_str = wx_api_util.WXAuth(signature=data['signature'],
                                         timestamp=data['timestamp'],
                                         nonce=data['nonce'],
                                         echostr=data['echostr'])
            return res_str

        elif request.method == 'POST':
            data = request.get_data() # .data
            # app.logger.info('POST_DATA:%s', data)
            reply = wx_api_util.ParseXML(data)
            # app.logger.info('reply:%s', reply)
            if reply:
                return reply
            return consts.WX_SUCC

    __builtin__.logger = app.logger
    return app



if __name__ == '__main__':
    app = CreateApp()
    app.run(debug=True)
