# -*- coding: utf-8 -*-

from .msg import Msg
import consts

class LinkMsg(Msg):
    def __init__(self, title='', desc='', url=''):
        super(LinkMsg, self).__init__()
        self.msg_type = consts.WX_MSG_LINK
        self.title = title
        self.desc = desc
        self.url = url

    def ParseXml(self, xml_data):
        super(LinkMsg, self).ParseXml(xml_data)
        title, desc, url = xml_data.find('Title'),  xml_data.find('Description'), xml_data.find('Url')
        self.title = title.text if title is not None else ''
        self.desc = desc.text if desc is not None else ''
        self.url = url.text if url is not None else ''

    def GenXmlInnerStr(self):
        base_str = super(LinkMsg, self).GenXmlInnerStr()
        link_str = """  <Title><![CDATA[{title}]]></Title>
  <Description><![CDATA[{desc}]]></Description>
 <Url><![CDATA[{url}]]></Url>""".format(
            title = self.title,
            desc = self.desc,
            url = self.url,
        )
        inner_str = '%s%s' % (base_str, link_str)
        return inner_str
