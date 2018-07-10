from django.db import models
from userinfo.models import UserInfo
from memberapp.models import Goods
# from userinfo.models import *


# Create your models here.
class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo, db_column='user_id', on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, db_column='goods_id', on_delete=models.CASCADE)
    ccount = models.SmallIntegerField('数量', null=False, default=1, db_column='cart_count')

    def __str__(self):
        return '购物车'

    class Meta:
        db_table = 'cartinfo'
        verbose_name = 'cartinfo'
        verbose_name_plural = verbose_name


ORDERSTATUS = (
    (1, '未支付'),
    (2, '已支付'),
    (3, '订单取消'),
)


class Order(models.Model):
    orderNo = models.CharField('订单号', max_length=20, null=False)
    orderdetail = models.TextField('订单详情', default='订单详情')
    adsname = models.CharField('收件人姓名', max_length=30, null=False)
    adsphone = models.CharField('收件电话', max_length=20, null=False)
    ads = models.CharField('收件地址', max_length=200, null=False)
    time = models.DateTimeField('下单时间', auto_now=True)
    acot = models.SmallIntegerField('总数')
    acount = models.DecimalField('总价', max_digits=8, decimal_places=2)
    orderstatus = models.SmallIntegerField('订单状态', choices=ORDERSTATUS, default=1)
    user = models.ForeignKey(UserInfo, db_column='user_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.orderNo

    class Meta:
        db_table = 'order'
        verbose_name = 'order'
        verbose_name_plural = verbose_name
