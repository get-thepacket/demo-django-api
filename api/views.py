from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def all_flights(request):
    if request.method 
    return HttpResponse('all-flights endpoint')

def hello(request):
    return HttpResponse('Hello World!')