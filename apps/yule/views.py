from django.shortcuts import render
from django.http import HttpResponse

from .sinanew import getSohuYule,getSohuYuleDetailPicture,getSohuYuleDetail

# Create your views here.
def index(request):
    # return HttpResponse(getNewsLinkUrl())
    url = 'https://v2.sohu.com/integration-api/mix/region/131?size=25&adapter=pc&secureScore=50&page={}&callback=jQuery1111'
    data = getSohuYule(url)
    return render(request, 'yule/index.html', data)

def detail(request,openurl='sss'):
    # print(openurl)
    url ='https:'+openurl
    s =getSohuYuleDetail(url)
    return render(request, 'yule/detail.html', {'data':s})

def detailPicture(request, openurl=''):
    url ='https:'+openurl
    data =getSohuYuleDetailPicture(url)
    return render(request, 'yule/detailp.html', {'data':data})

def page_not_found(request):
    return render(request,'404.html','')