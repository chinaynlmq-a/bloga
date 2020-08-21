from django.urls import path,re_path

from .views import index,detail,detailPicture,wylist,wybizdetail,wyBabyList,wyBabydetail,shHistoryLsit

urlpatterns = [
    path('', index, name='index'),
    # path('details/https:<path:openurl>', detail, name='details'),
    path('details', detail, name='details'),
    #path('pictures/https:<path:openurl>', detailPicture, name='detail_picture'),
    path('pictures', detailPicture, name='detail_picture'),
    path('biz/<int:page>', wylist, name='wylist'),
    path('bizdetail', wybizdetail, name='wybizdetail'),
    path('baby/<int:page>', wyBabyList, name='wyBabyList'),
    #path('babydetail/<path:url>', wyBabydetail, name='wyBabydetail'),
    #亲子详细
    path('babydetail', wyBabydetail, name='wyBabydetail'),
    #历史
    path('history', shHistoryLsit, name='shHistoryLsit')
    
    
    #path('pictures/', detailPicture, name='detail_picture')
    #re_path(r'^details/(?P<openurl>{*.})/$',detail, name='details')
]