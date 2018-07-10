from django.shortcuts import render, get_object_or_404
from .models import *
from django.db import DatabaseError
import logging
import random


# Create your views here.
def index(request):
    # 查询数据库全部分类和全部商品
    # 方案一
    # 按照分类名查询商品，并分别存储回传前端
    try:
        good_fruit_type = get_object_or_404(GoodsType, title='水果')
        fruit_goods = random.sample(list(good_fruit_type.goods_set.all()), 2)
    except DatabaseError as e:
        logging.warning(e)

    # 方案二
    types = GoodsType.objects.all()
    goods = Goods.objects.all()

    # 方案三
    types = GoodsType.objects.all()
    ac = []
    for type in types:
        b = {}
        b['type'] = type.title
        b['goods'] = random.sample(list(type.goods_set.all()), 2)
        ac.append(b)

    return render(request, 'index.html', {'good_list': locals()})


def detail_one(request):
    goodid = request.GET.get('goodid')
    goods = Goods.objects.get(id=goodid)
    return render(request, 'detail.html', {'goods': goods})