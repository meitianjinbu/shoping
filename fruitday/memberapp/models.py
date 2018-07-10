from django.db import models

# Create your models here.
class GoodsType(models.Model):
    title = models.CharField('分类名称', max_length=30, null=False)
    desc = models.CharField('描述', max_length=200, default='商品描述')
    isdelete = models.BooleanField('删除', default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'goodstype'
        verbose_name = 'goodstype'
        verbose_name_plural = verbose_name


class Goods(models.Model):
    title = models.CharField('商品名称', max_length=30, null=False)
    desc = models.CharField('描述', max_length=200, default='商品描述')
    unit = models.CharField('计量单位', max_length=30, null=False)
    price = models.DecimalField('商品价格', max_digits=8, decimal_places=2)
    picture = models.ImageField('商品图片', upload_to='static/images/goods', default='normal.png')
    detail = models.TextField('商品详情', default='商品详情')
    isdelete = models.BooleanField('删除', default=False)
    type = models.ForeignKey(GoodsType, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'goods'
        verbose_name = 'goods'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        if self.type.title == '水果':
            return '/detail/?goodid={}'.format(self.id)
        elif self.type.title == '肉类':
            return u'不爱吃'

