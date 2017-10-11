
from django.conf.urls import url
from . import views
#有参数的网址放在前面
urlpatterns = [

    url(r'^(.*)-(.*)-(.*)', views.students,name='getstu'),


]
