from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from goods.models import Goods, GoodsCategory, Banner

from rest_framework.views import APIView
from goods.serializers import GoodsSerializer, CategorySerializer, BannerSerializer
from .models import Goods
from rest_framework.response import Response

# class GoodsListView(View):
#     '''
#     商品列表
#     '''
#     def get(self, request, format=None):
#         goods = Goods.objects.all()
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)

from goods.serializers import GoodsSerializer
from .models import Goods
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import GoodsFilter

'''
drf中的APIView,GenericView,viewsets和router原理：
GenericViewSet
mixins源码解析：

'''


class GoodsPagination(PageNumberPagination):
    '''商品列表自定义分页'''
    # 默认每页显示个数
    page_size = 12
    # 可以动态改变每页显示的个数
    page_size_query_param = 'page_size'
    # 页码参数
    page_query_param = 'page'
    # 最多能显示多少页
    max_page_size = 100


class GoodsListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:商品列表，分页，搜索，过滤，排序
    retrieve:获取商品详情
    '''
    throttle_classes = (UserRateThrottle, AnonRateThrottle)
    # 这里必须定义一个默认的排序，否则 会报错
    queryset = Goods.objects.all().order_by('id')
    # 分页
    pagination_class = GoodsPagination
    # 序列化
    serializer_class = GoodsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    # 设置filter的类为我们自定义的类
    # 搜索
    search_fields = ('name', 'goods_brief', 'goods_desc')

    # 过滤
    filter_class = GoodsFilter

    # 排序
    ordering_fields = ('sold_num', 'shop_price')

    # 商品点击+1
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:
        商品分类列表数据
        mixins.ListModelMixin:显示queryset是数据
        mixins.RetrieveModelMixin:显示一个model对象
    viewsets:
    '''
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    首页轮播图
    '''
    quseyset = Banner.objects.all().order_by("index")
    serializer_class = BannerSerializer


# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
#     '商品列表页'
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

from .serializers import IndexCategorySerializer


class IndexCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    首页商品分类数据
    '''
    # 获取is_True(导航栏)里面的分类下的商品数据
    queryset = GoodsCategory.objects.filter(is_tab=True, name__in=["生鲜食品", "酒水饮料"])
    serializer_class = IndexCategorySerializer


from .models import HotSearchWords
from .serializers import HotWordsSerializer


class HotSearchsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''热搜'''
    queryset = HotSearchWords.objects.all().order_by("-index")
    serializer_class = HotWordsSerializer


