# _*_ coding:utf-8 _*_
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^register/', register_in, name='register'),
    url(r'^registerin/', register_, name='register_in'),
    url(r'^login/', login_in, name='login'),
    url(r'^loginin/', login_, name='login_in'),
    url(r'^logout/', logout, name='logout'),
    url(r'^addads/', add_ads_in, name='addads'),
    url(r'^addadsin/', add_ads_, name='addadsin'),
    url(r'^adslist/', user_ads, name='adslist'),
    url(r'^delads/', delete_ads, name='delads'),
]