# _*_ coding:utf-8 _*_
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^addintocart/', add_cart, name='addintocart'),
    url(r'^$', cart_info, name='cart'),
    url(r'^order/', order, name='order'),
    url(r'^addorder/', add_order, name='addorder'),
    url(r'^orderlist/', order_list, name='orderlist'),
    url(r'^delcart/', delete_cart, name='delcart'),
]