# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "survey_form/index.html")

def process(request):
    if request.method == 'POST':
        if not 'submission' in request.session:
            request.session['submission'] = 1
        else:
            request.session['submission'] += 1
        data = request.POST
        request.session['name'] = data.get('name')
        request.session['location'] = data.get('location')
        request.session['language'] = data.get('language')
        request.session['comments'] = data.get('comments')
    return redirect('/results')

def results(request):
    context = {
        'name': request.session['name'],
        'location' : request.session['location'],
        'language' : request.session['language'],
        'comments' : request.session['comments'],
    }
    return render(request,'survey_form/results.html',context)

def reset(request):
    request.session.clear()
    return redirect('/')



# def generate(request):
#     if 'attempt' in request.session:
#         request.session['attempt'] += 1
#     else:
#         request.session['attempt'] = 1 
#     print request.session['attempt']
#     word = ''
#     my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
#     for times in range (0, 14):
#         word = word + str(random.choice(my_letters))
#     words = {
#         'random_word': word
#     }
#     return render(request,'random_words/index.html',words)