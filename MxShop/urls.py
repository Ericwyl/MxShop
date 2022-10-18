
from django.urls import path, include, re_path
import xadmin
# from xadmin.plugins import xversion
# xadmin.autodiscover()
# xversion.reister_models()
# from xadmin import xadmin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
]
