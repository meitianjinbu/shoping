from django.db import models


# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(verbose_name='用户名', max_length=50, null=False)
    upassword = models.CharField('密码', max_length=200, null=False)
    email = models.CharField('邮箱', max_length=50, null=True)
    phone = models.CharField('手机号', max_length=20, null=False)
    time = models.DateTimeField(verbose_name='注册时间', auto_now=True)
    isban = models.BooleanField('禁用', default=False)
    isdelete = models.BooleanField('删除', default=False)

    def __str__(self):
        return self.uname

    class Meta:
        db_table = 'userinfo'
        verbose_name = 'userinfo'
        verbose_name_plural = verbose_name


class Address(models.Model):
    aname = models.CharField('收货人', max_length=50, null=False)
    ads = models.CharField('地址', max_length=200, null=False)
    phone = models.CharField('收件电话', max_length=20, null=False)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.aname

    class Meta:
        db_table = 'address'
        verbose_name = 'address'
        verbose_name_plural = verbose_name

    def get_delete_url(self):
        return '/user/delads/?adsid={}'.format(self.id)