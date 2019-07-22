from django.shortcuts import render
from django.http import HttpResponse
# coding:utf8
# Create your views here.

def myfirstpage(request):
    a=request.GET['a']
    b=request.GET['b']
    return  HttpResponse(str(a+b))