# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from time import strftime, localtime

def index(request):
    context = {
    "time": strftime("%B %d, %Y %I:%M %p", localtime())
    }
    return render(request,'time_display/index.html',context)

def time_display(request):
 return redirect('/')


