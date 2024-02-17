from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, friend!')


def about(request):
    return HttpResponse('I`am Piotr.')
