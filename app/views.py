from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def firstFbv(request):
    return HttpResponse('<h1>Harshad vali shaik</h1>')

def secondFbv(request):
    return HttpResponse('<h2><marquee>Python and Django Trainer</h2></marquee>')