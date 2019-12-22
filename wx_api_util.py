# -*- coding: utf-8 -*-
import hashlib
import consts
import logging
import xml.etree.ElementTree as ET
import private_consts


def WXAuth(signature, timestamp, nonce, echostr):
    try:
        token = private_consts.TOKEN

        ls = [token, timestamp, nonce]
        ls.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, ls)
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            return echostr
        else:
            return ""
    except Exception, e:
        logging.info('Traceback:%r', e)
        return str(e)




from msg_factory.text_msg import TextMsg
from msg_factory.msg import Msg
import wx_msg_pro

def ParseXML(we_data):
    if not we_data:
        return None
    xml_data = ET.fromstring(we_data)
    msg_type = xml_data.find('MsgType').text
    if msg_type == consts.WX_MSG_TEXT:
        msg = TextMsg()
        msg.ParseXml(xml_data)
        msg.content = '<a href="%s?oid=%s">%s</a>' % (consts.ReplyLinkOpRegister.URL,msg.from_user, consts.ReplyLinkOpRegister.TITLE) #
        reply_data = msg.Reply()
        # logger.info('-----------------reply_data:%r', reply_data)
        return reply_data
    else:
        logger.info('-----wd_data:%r', we_data)
        msg = Msg()
        msg.ParseXml(xml_data)
        text_msg = TextMsg()
        msg.CoverChildType(text_msg)
        text_msg.content = '您好，请通过菜单注册！'
        return text_msg.Reply()

def InitOrGetAccessToken():
    import urllib
    import time
    import access_token
    cur_time = int(time.time())
    access_dict = getattr(access_token, 'access_dict', None)
    if access_dict and access_dict['expires_in'] > cur_time:
        private_consts.ACCESS_TOKEN = access_dict['access_token']
        private_consts.ACCESS_TOKEN_TIME = access_dict['expires_in']
        return

    TEMPLATE = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}'
    url = TEMPLATE.format(appid=private_consts.APPID, secret=private_consts.APPSECRET)
    response = urllib.urlopen(url, proxies={})
    try:
        access_dict = eval(response.read())
    except Exception, e:
        logging.info('exception:e=%s', e)
    access_dict['expires_in'] += cur_time - 100

    private_consts.ACCESS_TOKEN = access_dict['access_token']
    private_consts.ACCESS_TOKEN_TIME = access_dict['expires_in']

    file_path = __file__
    file_path = file_path[: 1 + file_path.rfind('/')] + 'access_token.py'
    fout = file(file_path, 'w')
    fout.write('access_dict=%s' % access_dict)
    fout.close()
    reload(access_token)

if __name__ == '__main__':
    data = """
<xml>
  <ToUserName><![CDATA[toUser]]></ToUserName>
  <FromUserName><![CDATA[fromUser]]></FromUserName>
  <CreateTime>1348831860</CreateTime>
  <MsgType><![CDATA[text]]></MsgType>
  <Content><![CDATA[this is a test]]></Content>
  <MsgId>1234567890123456</MsgId>
</xml>
    """
    # print __file__
    #ParseXML(data)
    # GetAccessToken()