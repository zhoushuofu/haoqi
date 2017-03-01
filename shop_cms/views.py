# -*- coding:utf8 -*-
from django.shortcuts import render
from models import UserInfo

# Create your views here.

def index(request):
    context = {}  
    return render(request,'shop_cms/index.html',context)  

# 显示各列表信息
def lists(request, table):
    # 从根据不同的请求，来获取相应的数据,并跳转至相应页面
    data=[]
    sub_title='okokok'
    list_template='node_list.html'
    if table == 'node':
        #data = Node.objects.all()
        list_template = 'shop_cms/node_list.html'
        sub_title = '节点信息'
    if table == 'user':
        data = UserInfo.objects.all()
        list_template = 'shop_cms/line_list.html'
        sub_title = '线路信息'
    if table == 'device':
        # data = Device.objects.all()
        list_template = 'shop_cms/device_list.html'
        sub_title = '设备信息'
    # 建立context字典，将值传递到相应页面
    context = {
        'data': data,
        'table': table,
        'sub_title': sub_title,
    }
    # 跳转到相应页面，并将值传递过去
    return render(request, list_template, context)


# 用于增加资源
def add(request, table):
    # ...
    # 创建context来集中处理需要传递到页面的数据
    context = {
        'form': form,
        'table': table,
    }
    # 如果没有有效提交，则仍留在原来页面
    return render(request, 'add.html', context)

# 用于增加资源
def edit(request, table):
    # ...
    # 创建context来集中处理需要传递到页面的数据
    context = {
        'form': form,
        'table': table,
    }
    # 如果没有有效提交，则仍留在原来页面
    return render(request, 'add.html', context)

# 用于增加资源
def delete(request, table):
    # ...
    # 创建context来集中处理需要传递到页面的数据
    context = {
        'form': form,
        'table': table,
    }
    # 如果没有有效提交，则仍留在原来页面
    return render(request, 'add.html', context)