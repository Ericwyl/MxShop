from rest_framework import serializers
from .models import Goods,GoodsCategory,GoodsImage, Banner, HotSearchWords


'''serializer实现商品列表页'''
# class GoodsSerializer(serializers.Serializer):
#     '''required=True:默认表单字段不能为空'''
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_images = serializers.ImageField()


class CategorySerializer3(serializers.ModelSerializer):
    '''三级分类'''
    class Meta:
        model = GoodsCategory()
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    '''二级分类'''
    sub_cat = CategorySerializer3()



'''
实现商品列表页:使用ModelSerializer无需添加字段，直接使用Goods即可，比serializer方便，使用'__all__'方法可全部序列化
'''
class GoodsSerializer(serializers.ModelSerializer):
    #覆盖外键字段
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = '__all__'

#商品分类
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsSerializer
        fields = "__all__"

