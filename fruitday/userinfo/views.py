import logging

from django.contrib.auth.hashers import make_password, check_password
from django.db import DataError, DatabaseError

from userinfo.models import UserInfo, Address
from django.shortcuts import render, redirect


# Create your views here.
def register_in(request):
    return render(request, 'register.html')


def register_(request):
    # 判断提交方式是否为post
    if request.method == 'POST':
        new_user = UserInfo()
        # 获取注册信息
        new_user.uname = request.POST.get('user_name')
        # 判断用户是否存在
        users = UserInfo.objects.filter(uname=new_user.uname)
        if len(users) > 0:
            return render(request, 'register.html', {'message': 'Username existed!'})

        if request.POST.get('user_pwd') != request.POST.get('user_cpwd'):
            return render(request, 'register.html', {'message': 'two password are not the same!'})
        new_user.upassword = make_password(request.POST.get('user_pwd'), 'abc', 'pbkdf2_sha1')
        new_user.email = request.POST.get('email')
        new_user.phone = request.POST.get('phone')

        try:
            new_user.save()
        except DatabaseError as e:
            logging.warning(e)
            return redirect('/')
    return redirect('/user/register')


def login_in(request):
    return render(request, 'login.html')


def login_(request):
    if request.method == 'POST':
        user = UserInfo
        user.uname = request.POST.get('user_name')
        user.upassword = request.POST.get('user_pwd')
        try:
            users = UserInfo.objects.filter(uname=user.uname)
            if len(users) <= 0:
                return render(request, 'login.html', {'message': 'Username not existed!'})
            if not check_password(user.upassword, users[0].upassword):
                return render(request, 'login.html', {'message': 'Password is incorrect!'})
        except DatabaseError as e:
            logging.warning(e)
        request.session['user_id'] = users[0].id
        request.session['user_name'] = user.uname
        return redirect('/')
    return redirect('/user/login')


def logout(request):
    try:
        if request.session['user_name']:
            del request.session['user_name']
            del request.session['user_id']
    except KeyError as e:
        logging.warning(e)
    return redirect('/')


def add_ads_in(request):
    return render(request, 'addads.html')


def add_ads_(request):
    if request.method == 'POST':
        ads = Address()
        user_id = request.session.get('user_id')
        ads.user = UserInfo.objects.get(id=user_id)
        ads.aname = request.POST.get('aname')
        ads.ads = request.POST.get('ads')
        ads.phone = request.POST.get('phone')
        try:
            ads.save()
        except DatabaseError as e:
            logging.warning(e)
        return redirect('/')
    return redirect('/')


def user_ads(request):
    user_id = request.session.get('user_id')
    try:
        user = UserInfo.objects.get(id=user_id)
        adss = user.address_set.all()
    except DatabaseError as e:
        logging.warning(e)
        return redirect('/')
    return render(request, 'adslist.html', {'adss': adss})


def delete_ads(request):
    ads_id = request.GET.get('adsid')
    try:
        delads = Address.objects.get(id=ads_id)
        delads.delete()
    except DatabaseError as e:
        logging.warning(e)
    return redirect('/')

