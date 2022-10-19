
from django.urls import path, include, re_path
import xadmin
# from xadmin.plugins import xversion
# xadmin.autodiscover()
# xversion.reister_models()
# from xadmin import xadmin
from django.views.static import serve
from MxShop.settings import MEDIA_ROOT
from goods.view_base import GoodsListView
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    #文件
    path('media/<path:path>', serve,{'document_root':MEDIA_ROOT}),
    path('goods/', GoodsListView.as_view(), name='goods-list'),
    path('docs', include_docs_urls(title='天空八部之回首掏')),
    path('api-auth/', include('rest_framework.urls')),
]
