from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello")


def staff_list(request):
    pass
