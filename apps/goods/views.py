from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from goods.models import Goods

from rest_framework.views import APIView
from goods.serializers import GoodsSerializer
from .models import Goods
from rest_framework.response import Response


class GoodsListView(View):
    '''
    商品列表
    '''
    def get(self, request, format=None):
        goods = Goods.objects.all()
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)



