# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import * 

def index(request):
    users = User.objects.all()
    context = {
        "users":users
    }
    return render(request,'index.html', context)

def new(request): #PROCESSES THE INFO
    return render(request,'newuser.html')

def create(request, methods='POST'):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect("/new")
    else:  
       User.objects.create(first=request.POST["first"], last=request.POST["last"], email=request.POST["email"])
    return redirect('/')

def update(request, methods='POST'):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/edit/'+id)
    else:
        user = User.objects.get(id = id)
        user.first = request.POST['first']
        user.last = request.POST['last']
        user.email = request.POST['email']
        user.save()
        return redirect('/')    

def show(request, id): #THIS ROUTE RENDERS YOUR PROFILE PAGE
    user = User.objects.get(id=id) #gets the user from the database
    context = {
        "user" : user
    }
    return render(request,'profile.html', context)

def edit(request, id):#THIS ROUTE GIVES YOU A FORM TO EDIT A CURRENT USER
    # user_list = User.objects.filter(id=id)
    user = User.objects.get(id=id)
    # if len(user_list) > 0:
    context = {
        "user" : user
    }
    return render(request,'edit.html', context)

def update (request, id): #THIS ROUTE UPDATES THE SPECIFIC USER YOU HAVE REQUESTED TO EDIT FROM THE EDIT ROUTE
    user_list = User.objects.filter(id=id)
    if len(user_list) > 0:
        user = user_list[0]
        errors = User.objects.validate(request.POST)
        if len(errors) > 0:
            for error in errors:
                messages.error(request,error)
        else:
            user.first = request.POST['first']
            user.last = request.POST['last']
            user.email = request.POST['email']
            user.save()
        return redirect ("/"+id)
    else:
        messages.error(request, "No such User!")
        return redirect ("/")

def delete(request, id): #THIS ROUTE GIVES THE USER A FORM TO DESTORY A CURRENT USER
    User.objects.filter(id=id).delete()
    return redirect("/")