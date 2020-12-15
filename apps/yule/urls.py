from django.urls import path,re_path

from .views import index,detail,detailPicture,wylist,wybizdetail,wyBabyList,wyBabydetail,shHistoryLsit,auto_article,auto_savemw

urlpatterns = [
    #娱乐
    path('', index, name='index'),
    # path('details/https:<path:openurl>', detail, name='details'),
    path('details', detail, name='details'),
    #path('pictures/https:<path:openurl>', detailPicture, name='detail_picture'),
    path('pictures', detailPicture, name='detail_picture'),
    # 商业
    path('biz/<int:page>', wylist, name='wylist'),
    path('bizdetail', wybizdetail, name='wybizdetail'),
    # 亲子
    path('baby/<int:page>', wyBabyList, name='wyBabyList'),
    #path('babydetail/<path:url>', wyBabydetail, name='wyBabydetail'),
    # 亲子详细
    path('babydetail', wyBabydetail, name='wyBabydetail'),
    #历史
    path('history', shHistoryLsit, name='shHistoryLsit'),

    path('autoll', auto_article, name='auto_article'),
    #采集美文网址内容列表
    path('save_mw', auto_savemw, name='auto_savemw')
    
    
    #path('pictures/', detailPicture, name='detail_picture')
    #re_path(r'^details/(?P<openurl>{*.})/$',detail, name='details')
]