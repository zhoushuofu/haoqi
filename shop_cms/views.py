from django.shortcuts import render

# Create your views here.

def lists(request):
    data='hello world'
    context=dict(data=data)
    return render(request,'shop_cms/index.html',context)
