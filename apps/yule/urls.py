from django.urls import path,re_path

from .views import index,detail,detailPicture,wylist,wybizdetail

urlpatterns = [
    path('', index, name='index'),
    path('details/https:<path:openurl>', detail, name='details'),
    path('pictures/https:<path:openurl>', detailPicture, name='detail_picture'),
    path('biz/<int:page>', wylist, name='wylist'),
    path('bizdetail/<path:url>', wybizdetail, name='wybizdetail')
    #path('pictures/', detailPicture, name='detail_picture')
    #re_path(r'^details/(?P<openurl>{*.})/$',detail, name='details')
]