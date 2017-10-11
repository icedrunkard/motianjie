
from django.conf.urls import url
from . import views
#有参数的网址放在前面
urlpatterns = [

    url(r'^getdptsof', views.getdptsof,name='getdpts'),
    url(r'^', views.index,name='index'),

]
