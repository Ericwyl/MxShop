
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
from rest_framework.routers import DefaultRouter
from goods.views import GoodsListViewSet, CategoryViewSet, BannerViewset, IndexCategoryViewset, HotSearchsViewset
from django.views.generic import TemplateView


router = DefaultRouter()

#配置goods的url
router.register(r'goods', GoodsListViewSet, base_name="goods")
#配置Category的url
router.register(r'categorys', CategoryViewSet, base_name="categorys")
#配置首页轮播图的url
router.register(r'banners', BannerViewset, base_name="banners")
#配置热搜的url
router.register(r'hotsearchs', HotSearchsViewset, base_name="hotsearchs")
#首页系列商品展示url
router.register(r'indexgoods', IndexCategoryViewset, base_name="indexgoods")


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    #文件
    path('media/<path:path>', serve,{'document_root':MEDIA_ROOT}),
    path('goods/', GoodsListView.as_view(), name='goods-list'),
    path('docs', include_docs_urls(title='天空八部之回首掏')),
    path('api-auth/', include('rest_framework.urls')),
    #商品列表页
    path('^', include(router.urls)),
    #首页
    path('index/', TemplateView.as_view(template_name='index.html'), name='index'),


]
