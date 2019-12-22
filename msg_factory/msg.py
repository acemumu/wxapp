# -*- coding: utf-8 -*-

import time

class Msg(object):
    def __init__(self):
        super(Msg, self).__init__()
        self.msg_type = ''
        self.to_user = ''
        self.from_user = ''
        self.create_time = 0
        self.msg_id = 0
        self.org_xml_data = ''

    def ParseXml(self, xml_data):
        self.org_xml_data = xml_data
        self.msg_type = xml_data.find('MsgType').text
        self.to_user = xml_data.find('ToUserName').text
        self.from_user = xml_data.find('FromUserName').text
        self.create_time = int(xml_data.find('CreateTime').text)
        self.msg_id = long(xml_data.find('MsgId').text)

    def GenXmlInnerStr(self):
        inner_xml = """  <ToUserName><![CDATA[{toUser}]]></ToUserName>
  <FromUserName><![CDATA[{fromUser}]]></FromUserName>
  <CreateTime>{createTime}</CreateTime>
  <MsgType><![CDATA[{msgType}]]></MsgType>""".format(
            toUser=self.to_user,
            fromUser=self.from_user,
            createTime=self.create_time,
            msgType=self.msg_type,
        )
        return inner_xml

    def CreateWholeSendXmlData(self):
        inner_str = self.GenXmlInnerStr()
        xml_data = """<xml>%s</xml>""" % inner_str
        return xml_data

    def Reply(self):
        self.create_time = int(time.time())
        self.from_user, self.to_user = self.to_user, self.from_user
        xml_data = self.CreateWholeSendXmlData()
        return xml_data

    def CoverChildType(self, child_msg):
        # child_msg.msg_type = self.msg_type
        child_msg.to_user = self.to_user
        child_msg.from_user = self.from_user
        child_msg.create_time = self.create_time
        child_msg.msg_id = self.msg_id



