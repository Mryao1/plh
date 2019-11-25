from django.contrib import admin
from django.urls import path,re_path
#这里和课程中的情况不一样！！！！！！from django.conf.urls import url这句话在这个环境中是不对的

from myapp import views

urlpatterns = [
    path('',views.index),
    path('index/', views.index),#注意这里不是url[……]，而是path【……】！！！！！
    path('register/',views.index),
    path('upload/',views.upload),#注意这里不能是upload/!!!没有斜杠！！！
]
