from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<i><h1>Hey there i am Laban</h1><i>")