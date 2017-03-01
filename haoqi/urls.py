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

]
