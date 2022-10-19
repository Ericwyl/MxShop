#为了区分django和djangorest的view，利用django的view实现返回json数据

from django.views.generic import View
from goods.models import Goods
import json


class GoodsListView(View):
    def get(self, request):
        #通过django的view实现商品列表页
        json_list = []
        #获取所有商品
        goods = Goods.objects.all()

        # for good in goods:
        #     json_dict = {}
        #     #获取商品的每个字段,键值对形式
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)

        #上面是把model中的几个字段进行dict化，下面这个使用model_to_dict进行所有字段dict化，但是出现问题：ImageFieldFile和add_time字段无法dict化,故最后采用serializer
        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)


        from django.core import serializers
        from django.http import HttpResponse
        from django.http import JsonResponse

        json_date = serializers.serialize('json', goods)
        json_date = json.loads(json_date)
        return JsonResponse(json_date, safe=False)

        #返回json，一定要指定类型content_type='application/json'
        # return HttpResponse(json.dumps(json_list), content_type='application/json')


