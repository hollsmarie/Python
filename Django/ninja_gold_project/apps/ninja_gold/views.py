# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from random import randint 
from time import gmtime, strftime

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    print request.session['count']
    if 'activity' not in request.session:
        request.session['activity'] = []
    print request.session ['activity']
    return render(request, "ninja_gold/index.html")

def process(request):
    if 'Farm' in request.POST['place']:
        gold = randint(10, 20)
        request.session['count'] += gold
        request.session['activity'].append('Earned {} golds from the Farm!'.format(request.session['count']))
        print "FARM WORKS"
    
    if 'Cave' in request.POST['place']:
        gold = randint(5, 10)
        request.session['count'] += gold
        request.session['activity'].append('Earned {} golds from the Cave!'.format(request.session['count']))
        print "CAVE WORKS"
    

    if 'House' in request.POST['place']:
        gold = randint(2, 5)
        request.session['count'] += gold
        request.session['activity'].append('Earned {} golds from the House!'.format(request.session['count']))
        print "HOUSE WORKS"

    if 'Casino' in request.POST['place']:
        gold = randint(-50, 50)
        request.session['count'] += gold
        request.session['activity'].append('Earned {} golds from the Casino!'.format(request.session['count']))
        print "CASINO WORKS", gold 

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
