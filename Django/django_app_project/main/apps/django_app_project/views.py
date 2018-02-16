# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
def index (request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "ourApp/index.html", context)


def new (request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create (request):
    # if request.method == "POST":
	# print "*"*50
	# print request.POST
    # print request.POST['name']
    # print request.POST['desc']
    #     request.session['name'] = "test"  # more on session below
    # print "*"*50
	#     return redirect("/")
	# else:
	return redirect("/")

def show (request):
    response = "placeholder to display blog {{number}}"
    return HttpResponse(response)

def edit (request):
    response = "placeholder to display edit blog {{number}}"
    return redirect('/edit')

def destroy (request):
    response = "placeholder to display blog {{number}}"
    return redirect('/')
