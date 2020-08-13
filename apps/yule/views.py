from django.shortcuts import render
from django.http import HttpResponse

from .sinanew import getSohuYule,getSohuYuleDetail

# Create your views here.
def index(request):
    # return HttpResponse(getNewsLinkUrl())
    url = 'https://v2.sohu.com/integration-api/mix/region/131?size=25&adapter=pc&secureScore=50&page={}&callback=jQuery1111'
    data = getSohuYule(url)
    return render(request, 'yule/index.html', data)

def detail(request):
    s =getSohuYuleDetail('https://www.sohu.com/a/412833871_120161664?scm=1002.280027.0.0-0')
    return render(request, 'yule/detail.html', {'data':s})