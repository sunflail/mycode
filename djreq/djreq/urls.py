#!/usr/bin/python3

# imports from Django
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('astro/', views.astro),    # access by proxy api.open-notify.org/astros.json
    path('nasa/', views.nasa),      # access by proxy api.nasa.gov
    path('pokemon/<str:name>', views.pokemon)
]
