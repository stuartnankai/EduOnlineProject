# encoding: utf-8
__author__ = 'eddyrain '
__date__ = '2018/11/06 0009 08:02'

import xadmin

from .models import EmailVerifyRecord


# 创建admin的管理类,这里不再是继承admin，而是继承object
class EmailVerifyRecordAdmin(object):
    pass

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
