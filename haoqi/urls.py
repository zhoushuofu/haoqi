# -*- coding:utf8 -*-
"""haoqi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import shop_cms.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', shop_cms.views.index), 
    url(r'^lists/(?P<table>[0-9a-zA-Z]*)/$', shop_cms.views.lists,name='lists'), 
    url(r'^add/(?P<table>[0-9a-zA-Z]*)/$', shop_cms.views.add,name='add'), 
    url(r'^edit/(?P<table>[0-9a-zA-Z]*)/$', shop_cms.views.edit,name='edit'), 
    url(r'^delete/(?P<table>[0-9a-zA-Z]*)/$', shop_cms.views.edit,name='delete'), 
    url(r'^create_shop$', shop_cms.views.create_shop,name='create_shop'), 
    url(r'^my_shop/(?P<user_id>[0-9a-zA-Z]*)$', shop_cms.views.my_shop,name='my_shop'), 
    #用户登陆列表
    #用户登陆
    url(r'login/', shop_cms.views.login, name='login'),
    #用户退出
    url(r'logout/', shop_cms.views.logout, name='logout'),
    #密码修改
    url(r'password_change/', shop_cms.views.password_change, name='password_change'),
]
