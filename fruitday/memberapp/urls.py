# _*_ coding:utf-8 _*_
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
]