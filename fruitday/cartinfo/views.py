import datetime
import logging

from django.db import DatabaseError
from django.shortcuts import render, redirect

from memberapp.models import Goods
from userinfo.models import UserInfo, Address
from .models import CartInfo, Order

import json
from django.http import HttpResponse


# Create your views here.
def add_cart(request):
    # 获取前端的数据（商品id，商品数量)
    # 获取用户的id
    new_cart = CartInfo()
    goods_id = request.GET.get('goodsid')
    goods_count = request.GET.get('gcount')
    user_id = request.session.get('user_id')

    goods = Goods.objects.filter(id=goods_id)
    user = UserInfo.objects.get(id=user_id)
    if len(goods) > 0:
        new_cart.user = user
        new_cart.goods = goods[0]
    else:
        content = {'status': 'OK', 'text': '无该商品'}
        return HttpResponse(json.dumps(content))
        # return render(request, 'index.html')
    new_cart.ccount = int(goods_count)
    try:
        oldgoods = CartInfo.objects.filter(user=user_id, goods=goods_id)
        if len(oldgoods) > 0:
            oldgoods[0].ccount += new_cart.ccount
            oldgoods[0].save()
        else:
            new_cart.save()
    except DatabaseError as e:
        logging.warning(e)
    content = {'status': 'OK', 'text': '添加成功'}
    return HttpResponse(json.dumps(content))
    # return redirect('/')


def cart_info(request):
    user_id = request.session.get('user_id')
    find_goodss = CartInfo.objects.filter(user_id=user_id)
    return render(request, 'cart.html', locals())


def order(request):
    user_id = request.session.get('user_id')
    adss = Address.objects.filter(user=user_id)
    content = {'adss': adss}
    return render(request, 'order.html', content)

def add_order(request):
    user_id = request.session.get('user_id')
    order = Order()
    order.user = UserInfo.objects.get(id=user_id)
    order.orderdetail = request.POST.get('acot')
    order.adsname = request.POST.get('adsname')
    order.ads = request.POST.get('ads')
    order.adsphone = request.POST.get('adsphone')
    acot = 0
    acount = 0.0
    order.orderNo = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    print(json.loads(order.orderdetail))
    for goods in json.loads(order.orderdetail):
        count = int(goods['count'])
        price = float(goods['price'])
        acot += count
        acount += price * count
    order.acot = acot
    order.acount = acount
    try:
        order.save()
    except DatabaseError as e:
        logging.warning(e)
        return redirect('/')
    content={'status': 'OK'}
    return HttpResponse(json.dumps(content))


def order_list(request):
    user_id = request.session.get('user_id')
    orders = Order.objects.filter(user_id=user_id)
    for order in orders:
        order.orderdetail = json.loads(order.orderdetail)
    return render(request, 'orderlist.html', {'orders': orders})


def delete_cart(request):
    user_id = request.session.get('user_id')
    try:
        carts = CartInfo.objects.filter(user_id=user_id)
        for cart in carts:
            cart.delete()
    except DatabaseError as e:
        logging.warning(e)
    content = {'status': 'OK', 'msg': '删除成功'}
    return HttpResponse(json.dumps(content))
