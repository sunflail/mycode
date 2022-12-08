#!/usr/bin/python3

# python3 -m pip install requests
import requests

# python3 -m pip install Django
from django.http import JsonResponse    # replaces "import json"

# API to lookup - Django will proxy the request for us
ASTROAPI = "http://api.open-notify.org/astros.json"
    
# https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY
NASAAPI = "https://api.nasa.gov/planetary/apod?api_key="

# Your NASA API key goes here
# in production this should be set as an environmental variable
# APIKEY = "DEMO_KEY"

POKEAPI = "https://pokeapi.co/api/v2/pokemon/"

def astro(request):    
    res = requests.get(ASTROAPI)
    return JsonResponse(res.json())  # abstraction to return json

def nasa(request):
    # pass in /?apikey=key when calling
    key = request.GET.get("apikey")
    res = requests.get(f"{NASAAPI}{key}")
    return JsonResponse(res.json()) # abstraction to return json

def pokemon(request, name):
    res = requests.get(f"{POKEAPI}{name}")
    return JsonResponse(res.json())
