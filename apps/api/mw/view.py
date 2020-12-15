from rest_framework import serializers,viewsets,mixins
from rest_framework.views import APIView
from rest_framework.response import Response
# 分页
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from yule.models import MwArticleList


'''
page_query_param：表示url中的页码参数
page_size_query_param：表示url中每页数量参数
page_size：表示每页的默认显示数量
max_page_size：表示每页最大显示数量，做限制使用，避免突然大量的查询数据，数据库崩溃
'''
#自定义分页类
class MyPageNumberPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 15
    page_size_query_param = 'size'
    page_query_param = 'page'

#序列化
class MwListSerializer(serializers.ModelSerializer):
  class Meta:
    model= MwArticleList
    fields = '__all__'

class MwListSet(mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = MwArticleList.objects.all()
    serializer_class = MwListSerializer
    pagination_class = LimitOffsetPagination


'''
首先需要实例化我们定义的分页类
并且对实例化类进行传参控制
最后将分页后的对象作序列化
'''

class MwListViews(APIView):
  def get(self,request,*args,**kwargs):
    pass
    # queryset = MwArticleList.objects.all()
    # serializer_class = MwListSerializer
    # permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
  

  # def get(self,request,*args,**kwargs):
  #   #roles = MwArticleList.objects.get_queryset().order_by('id')
  #   roles = MwArticleList.objects.all().order_by('id')

  #   # 实例化分页
  #   page = MyPageNumberPagination()
  #   page_roles = page.paginate_queryset(queryset=roles, request=request, view=self)
  #   # page_roles = page.paginate_queryset(roles, request=request, view=self)
  #   roles_ser = MwListSerializer(instance=page_roles, many=True)
  #   #roles_ser = MwListSerializer(page_roles, many=True)
  #   return page.get_paginated_response(roles_ser.data)  # 返回前后页url
  #   # return Response(roles_ser.data)