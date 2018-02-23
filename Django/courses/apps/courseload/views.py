# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from .models import *

from ..loginReg.models import *

from django.shortcuts import render, HttpResponse, redirect

def index(request): #this route shows us our course page
    course = Course.objects.all()
    context = {
        "courses":course
    }
    return render(request,'courseload/index.html', context)

def add(request, methods='POST'):
    errors = Course.objects.validate(request.POST)
    if len(errors) > 0:
        for error in errors.iteritems:
            messages.error(request, error)
        return redirect(reverse('courses:index'))
    else:  
       Course.objects.create(courseName=request.POST["courseName"], courseDescription=request.POST["courseDescription"])
    return redirect(reverse('courses:index'))

def delete(request, id):
    context = {
        "course" : Course.objects.get(id=id)
    }
    return render(request,'courseload/delete.html', context)

def addFaves(request, id):
    currentUser = User.objects.get(id=request.session['userid'])
    fave = Course.objects.get(id=id)
    fave.favorites.add(currentUser)
    return redirect(reverse('courses:index'))

def profile(request, id):
    currentUser = User.objects.get(id=id)
    favorites = currentUser.userFaves.all
    context = {
        "favorites" : favorites
    }
    return render(request,'courseload/profile.html', context)

def destroy(request, id): 
    Course.objects.get(id=int(id)).delete()
    return redirect(reverse,('courses:index'))
