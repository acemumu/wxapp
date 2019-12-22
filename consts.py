# -*- coding: utf-8 -*-

WX_MSG_TEXT = 'text'
WX_MSG_LINK = 'link'
WX_MSG_IMAGE = 'image'
WX_MSG_VOICE = 'voice'

WX_SUCC = 'success'

DB_NAME = 'wxdb'
COL_OP_INFO = 'op_info'
DB_IP = '127.0.0.1'
DB_PORT = 30000


#文字信息处理
REGISTER_OP_INFO = '手术登记'
DOC_REPLY_INVALID_TEXT = """输入信息无法识别，请输入：%s""" % REGISTER_OP_INFO
class ReplyLinkOpRegister(object):
    TITLE = '手术登记（点击，转发无效）'
    DESC = '网报百度新研制的全家桶，转发无效'
    URL = 'http://rktfew.natappfree.cc/cgi-bin/wx_cgi/auth/login'


TEMPLATE_MSG_POST_URL = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s'
TEMPLATE_TITLE = 'Dear {name}'



