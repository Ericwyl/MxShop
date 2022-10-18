import xadmin


from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    '''添加主题功能'''
    enablee_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    '''全局配置，后台管理标题和页脚'''
    site_title = 'ericwei`s MxShop后台'
    site_footer = "我是页脚"
    #菜单收缩
    menu_style = "accordion"



