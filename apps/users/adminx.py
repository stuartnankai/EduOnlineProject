# encoding: utf-8
__author__ = 'eddyrain '
__date__ = '2018/11/06 0009 08:02'

import xadmin
from xadmin import views
from .models import EmailVerifyRecord,Banner


# 创建admin的管理类,这里不再是继承admin，而是继承object
class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email','send_type', 'send_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['code', 'email', 'send_type']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)



# 创建banner的管理类
class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']


# 将model与admin管理器进行关联注册
xadmin.site.register(Banner, BannerAdmin)


# 创建X admin的全局管理器并与view绑定。
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

# 将全局配置管理与view绑定注册
xadmin.site.register(views.BaseAdminView, BaseSetting)


# x admin 全局配置参数信息设置
class GlobalSettings(object):
    site_title = "Eddyrain"
    site_footer = "eddyrain's website"
    # 收起菜单
    menu_style = "accordion"
# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView, GlobalSettings)
