#!/usr/bin/python3

# imports from Django
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound

# This view will return a 404 response
def ierror(request):
    return HttpResponseNotFound("Page was not found")
    
def success(request):
    return HttpResponse("Page was found")

def customheader(request):
    x = {}
    x['learning'] = 'Django' # string:string
    x['speed'] = 55          # string:integer
    
    return HttpResponse(headers=x)  # adds our custom headers to the response

def customcode(request):
    return HttpResponse("Working on that", status=201)  # return teh response code 201 "created"

def teapot(request):
    return HttpResponse("Best code", status=418)

def upgrade(request):
    return HttpResponse("Upgrade required", status=426)

def served(request):
    x = {}
    x["You've been"] = "served"
    x["Oh Sweet"] = "child o' mine"
    return HttpResponse(headers=x)