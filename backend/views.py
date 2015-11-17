# coding:utf8
from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
import json
from django.conf import settings
from django.core.cache import cache
import random
import logging
from models import *
import datetime
import os

# Create your views here.

logger = logging.getLogger(__name__)

def createSession(request,user):
    if not request.session.get("username",False):
        request.session['username'] = user
    else:
        return False
    return True

def loginNeed(func):
    def _loginNeed(request):
        if not request.session.get("username",False):
            return JsonResponse({
                "error_no" : "1"    
            })
        else:
            return func(request)
    return _loginNeed

def loginAction(request):
    user = request.GET['uname']
    password = request.GET['upwd']
    try:
        u = User.objects.get(username=user)
        if(u.password == password):
            createSession(request,user)
        else :
            return JsonResponse({
                "error_no" : "1",
                "message":"wrong password"
            })
        return JsonResponse({
            "error_no":"0"
        })
    except Exception,e:
        return JsonResponse({
            "error_no":"1",
            "message":"exception happened"
        })

@loginNeed
def quitAction(request):
    if not request.session.get("username",False):
        return JsonResponse({
            "status":"fail"
        })
    else:
        request.session['username'] = ""
        return JsonResponse({
            "status":"success"
        })

def getNewsList(request):
    n = News.objects.all()
    data = []
    map(lambda i:data.append({"id":i.id,"title":i.title,"desc":i.desc}),n)
    return JsonResponse({
        "error_no" : "0",
        "data" : data
    })

@loginNeed
def addNews(request):
    title = request.POST.get("title")
    desc = request.POST.get("desc")
    n = News(title=title,desc=desc)
    n.save()
    return JsonResponse({
        "error_no" : "0"    
    })

@loginNeed
def editNews(request):
    id = request.POST.get("id")
    title = request.POST.get("title")
    desc = request.POST.get("desc")
    n = News(id=id,title=title,desc=desc)
    n.save()
    return JsonResponse({
        "error_no" : "0"    
    })

@loginNeed
def deleteNews(request):
    id = request.POST.get("id")
    n = News.objects.get(id=id)
    n.delete()
    return JsonResponse({
        "error_no" : "0"    
    })

def getNewsById(request):
    id = request.GET.get("id")
    n = News.objects.get(id=id)
    data = {"id":n.id,"title":n.title,"desc":n.desc}
    return JsonResponse({
        "error_no" : "0",
        "data" : data
    })

def getProductList(request):
    n = Product.objects.all()
    data = []
    map(lambda i:data.append({"id":i.id,"title":i.title,"desc":i.desc}),n)
    return JsonResponse({
        "error_no" : "0",
        "data" : data
    })

@loginNeed
def addProduct(request):
    title = request.POST.get("title")
    desc = request.POST.get("desc")
    n = Product(title=title,desc=desc)
    n.save()
    return JsonResponse({
        "error_no" : "0"    
    })

@loginNeed
def editProduct(request):
    id = request.POST.get("id")
    title = request.POST.get("title")
    desc = request.POST.get("desc")
    n = Product(id=id,title=title,desc=desc)
    n.save()
    return JsonResponse({
        "error_no" : "0"    
    })

@loginNeed
def deleteProduct(request):
    id = request.POST.get("id")
    n = Product.objects.get(id=id)
    n.delete()
    return JsonResponse({
        "error_no" : "0"    
    })

def getProductById(request):
    id = request.GET.get("id")
    n = Product.objects.get(id=id)
    data = {"id":n.id,"title":n.title,"desc":n.desc}
    return JsonResponse({
        "error_no" : "0",
        "data" : data
    })
@loginNeed
def editCul(request):
    id = request.POST.get("id")
    title = request.POST.get("title")
    desc = request.POST.get("desc")
    n = Option(id=id,title=title,desc=desc)
    n.save()
    return JsonResponse({
        "error_no" : "0"    
    })
def getCulById(request):
    id = request.GET.get("id")
    n = Option.objects.get(id=id)
    data = {"id":n.id,"title":n.title,"desc":n.desc}
    return JsonResponse({
        "error_no" : "0",
        "data" : data
    })
def getCulList(request):
    n = Option.objects.all()
    data = []
    map(lambda i:data.append({"id":i.id,"title":i.title,"desc":i.desc}),n)
    return JsonResponse({
        "error_no" : "0",
        "data" : data
    })
