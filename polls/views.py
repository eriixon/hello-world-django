from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse("Hello, world, from Index")


def hello(request):
    return HttpResponse("Hakuna matata")
