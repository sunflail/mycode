#!/usr/bin/python3

# imports from Django
from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random

# This view will return "Welcome to the Phoenix Cafe!" as text
def welcome(request):
    return HttpResponse("Welcome to the Phoenix Cafe!")

def sleepy(request):
    return HttpResponse("Z-z-z-z-z-z!")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)  # we are not returning a static string

def rand(request):
    result = random.random() * 100
    html = "<html><body>Random float is %f.</body></html>" % result
    return HttpResponse(html)