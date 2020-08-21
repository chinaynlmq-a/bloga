from django.shortcuts import render
from django.http import HttpResponse
from urllib import parse

from yule.souhu_model import GetSouhu
from .sinanew import getSohuYule,getSohuYuleDetailPicture,getSohuYuleDetail
from .wy_biz import getWyBizList,getWyBizListDetail
from .wy_baby import *

# Create your views here.
# 网易商业
def wylist(request,page=1):
    data = getWyBizList(page)
    return render(request, 'yule/wy_biz.html', {'data':data})
# 网易商业详细页面
def wybizdetail(request,url):
    #url = parse.unquote(url)
    data = getWyBizListDetail(parse.unquote(url))
    return render(request, 'yule/wy_biz_detail.html', {'data':data})

# 网易亲子
def wyBabyList(request,page=1):
    data = getWyBabyList(page)
    return render(request, 'yule/wy_baby.html', {'data':data})
# 网易商业详细页面
def wyBabydetail(request,url):
    #url = parse.unquote(url)
    data = getWyBabyListDetail(parse.unquote(url))
    return render(request, 'yule/wy_baby_detail.html', {'data':data})
# 搜狐娱乐
def index(request):
    # return HttpResponse(getNewsLinkUrl())
    # url = 'https://v2.sohu.com/integration-api/mix/region/131?size=25&adapter=pc&secureScore=50&page={}&callback=jQuery1111'
    # data = getSohuYule(url)
    data = GetSouhu().get_list('131')
    return render(request, 'yule/index.html', data)

# 搜狐详细页面
def detail(request):
    if request.method=='GET':
        url =request.GET.get('getUrl',default='110')
    #url ='https:'+openurl
    s =getSohuYuleDetail(parse.unquote(url))
    return render(request, 'yule/detail.html', {'data':s})

#搜狐历史列表
def shHistoryLsit(request):
    data =GetSouhu().get_list()
    return render(request, 'yule/index.html', data)

def detailPicture(request):
    if request.method=='GET':
        url =request.GET.get('getUrl',default='110')
    data =getSohuYuleDetailPicture(parse.unquote(url))
    return render(request, 'yule/detailp.html', {'data':data})

def page_not_found(request):
    return render(request,'404.html','')