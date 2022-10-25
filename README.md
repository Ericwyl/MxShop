'''
测试文件
切换到“我的分支”
步骤：
创建分支:git branch wylbranch
查看分支：git branch
切换到我的分支：git checkout wylbranch

#=====================
切换到自己的分支之后
开发自己的代码
1、提交之前，拉取项目上主分支最新的代码：git pull或者执行git pull -origin master
如果有冲突，自己想办法解决
2、提交已经写好并自测过的代码：git add 已经写好的代码.py     
3、git commit -m '代码的文字说明'
4、提交到自己的分支上：git push --set-upstream prigin wylbranch

后面你的经理或者CTO会登录gitlab进行代码审查、合并


一、Goods模块model：
goods模块
商品分类表:GoodsCategory
宣传商标表：GoodsCategoryBrand
商品表:Goods
商品轮播图表：GoodsImage
首页轮播图表:Banner
商品广告和热搜:IndexAd
搜索栏下方热搜词:HotSearchWords

1.商品模块是一个三级级联操作(一类二类三类)，需要设置一个商品分类表,以及父类作为外键指向自己(父类跟子类是一对多的关系，在
django中使用models.Foreignkey("self")来表示)
2.某一个大类下面都有不同的宣传品牌及商标，需要创建一个宣传商标表,设置外键关联商品分类表
3.每种商品的数据，创建一个商品表，父类别下面有多个商品，外键关联商品分类表
4.商品详情页面有商品的轮播图，创建商品轮播图表，设置外键关联商品表，一对一关系
5.每种商品都有商品广告及热搜，用于索引，创建商品广告表，两个外键，商品表、分类表
6.搜索栏下方有热搜词显示，创建热搜表，无需外键，索引即可
7.首页轮播的商品，直接外键关联到商品表即可
二、商品模块model已经设计好，之后开始进行序列化以及编写view
1.goods使用model_to_dict所有商品进行dict，但是出现ImageFieldFile和add_time字段不能序列化
2.使用django  serializer进行序列化,发现字段序列化是定死的，想要重组的话非常麻烦，故改变方式
3.编写路由,然后使用Apiview的方式进行系列化
4.编写serializer.py文件，一个分类序列化表，一个商品序列化表(类中覆盖外键字段，这样可以以‘类别->商品详细字段’的形式把数据嵌套展示出来
)，至此，序列化完成
5.使用GenericView实现商品列表页，GenericView比APIview强大，一般编写视图，需要跟mixin搭配使用
GenericView中的方法:
    CreateAPIView(创建对象):
    ListAPIView(批量查询)、
    RetrieveAPIView(单个查询)、
    DestroyAPIView(删除对象)、
    UpdateAPIView（修改对象）

mixins总共有五种：
　　CreateModelMixin
　　ListModelMixin
　　UpdateModelMixin
　　RetrieveModelMixin
　　DestoryModelMixin

generics起到了将mixins类里面的方法和http请求结合起来的作用
class ListAPIView(mixins.ListModelMixin,GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



'''