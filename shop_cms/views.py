# -*- coding:utf8 -*-
from django.shortcuts import render
from models import UserInfo
from django.db import connection
import json
from django.http import HttpResponseRedirect 

from django.contrib.auth import views
from django.contrib.auth.decorators import login_required

# Create your views here.
def __open_connection():
    return connection.cursor()

# close a database connection
def __close_connection(cursor):
    connection.close()


def dict_fetchall(cursor):
    # 将游标返回的结果保存到一个字典对象中
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
        ]
db_handle = __open_connection()


def exe_sql(sql):
    db_handle.execute(sql)
    res=dict_fetchall(db_handle)
    return res

def get_insert_shop_id():
    sql='''insert into shopinfo_tickets64_innodb() values()'''
    result = exe_sql(sql)
    sql='''select last_insert_id() as id'''
    res=exe_sql(sql)
    shop_id=res[0]['id']
    return shop_id

@login_required  
def index(request):
    context = {}
    return render(request,'shop_cms/create_shop.html',context)  

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
        return HttpResponseRedirect("/admin") 
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

@login_required  
def create_shop(request):
    if request.method=='POST':
        title=request.POST['title']
        user_id=request.POST['user_id']
        icon_photo=request.POST['icon_photo']
        photo_ids=request.POST['photo_ids']
        intro=request.POST['intro']
        open_time=request.POST['open_time']
        phone=request.POST['phone']
        address=request.POST['address']
        brands=request.POST['brands']
        longitude=request.POST['longitude']
        latitude=request.POST['latitude']
        city=request.POST['city']
        province=request.POST['province']
        shop_id=get_insert_shop_id()
        sql = '''insert into shop_info(shop_id,user_id,title,icon_photo,desc_photos,intro,location,
                open_time,phone,brands,longitude,latitude,city,province)
                values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')''' % (
            shop_id, user_id,title, icon_photo, photo_ids, intro, address, open_time, phone,
            brands, longitude, latitude, city, province)
        print sql
        exe_sql(sql)
        return HttpResponseRedirect("/my_shop/%s"%user_id) 


@login_required  
def my_shop(request,user_id):
    user_id=int(user_id)
    sql='''select shop_id,title,user_id,location,open_time from shop_info where user_id=%d and status=0'''%user_id
    res=exe_sql(sql)
    context=res
    print res
    context = {
        'data': res,
        'table': 'table',
        'sub_title': '我的商店',
    }
    return render(request,'shop_cms/myshop.html',context)

#用户登陆选项，所有的函数将会返回一个template_response的实例，用来描绘页面，同时你也可以在return之前增加一些特定的功能
#用户登陆
def login(request):
    #extra_context是一个字典，它将作为context传递给template，这里告诉template成功后跳转的页面将是/index
    template_response = views.login(request, extra_context={'next': '/'})
    return template_response

#用户退出
def logout(request):
    #logout_then_login表示退出即跳转至登陆页面，login_url为登陆页面的url地址
    template_response = views.logout_then_login(request,login_url='/login')
    return template_response

#密码更改
def password_change(request):
    #post_change_redirect表示密码成功修改后将跳转的页面.
    template_response = views.password_change(request,post_change_redirect='/')
    return template_response

