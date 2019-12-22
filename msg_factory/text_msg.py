# -*- coding: utf-8 -*-
from .msg import Msg
import consts

class TextMsg(Msg):
    def __init__(self):
        super(TextMsg, self).__init__()
        self.msg_type = consts.WX_MSG_TEXT
        self.content = '您好'

    def ParseXml(self, xml_data):
        super(TextMsg, self).ParseXml(xml_data)
        content = xml_data.find('Content')
        import logging
        self.content = content.text if content is not None else ''

    def GenXmlInnerStr(self):
        base_str = super(TextMsg, self).GenXmlInnerStr()
        inner_str = """{base}
  <Content><![CDATA[{content}]]></Content> 
        """.format(base=base_str, content=self.content)

        return inner_str



