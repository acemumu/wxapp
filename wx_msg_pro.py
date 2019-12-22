# -*- coding: utf-8 -*-

import consts

def ProcessTextMsg(msg):
    if msg.content == consts.REGISTER_OP_INFO:
        from msg_factory.link_msg import LinkMsg
        link_msg = LinkMsg(title=consts.ReplyLinkOpRegister.TITLE, url=consts.ReplyLinkOpRegister.URL, desc=consts.ReplyLinkOpRegister.DESC)
        msg.CoverChildType(link_msg)
        return link_msg
    msg.content = consts.DOC_REPLY_INVALID_TEXT
    return msg

