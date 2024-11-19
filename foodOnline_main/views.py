from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello World!')

def index(request):
    return HttpResponse("Hello")

def about(request):
    return HttpResponse("About Hello")

