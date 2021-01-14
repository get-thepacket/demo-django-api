from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import Flights
from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.
def all_flights(request):
    if request.method == "GET":
        f = Flights.objects.all()
        json_data = serializers.serialize('json',f) # convert the QuerySet to json formatted data
        return JsonResponse(json_data, safe=False)
    else:
        res = {
            "message":"Invalid request"
        }
        return JsonResponse(res)

@csrf_exempt
def book_flight(request):
    if(request.method == "POST"):
        print(list(request.POST.items()))
        return HttpResponse("OK!")

def hello(request):
    return HttpResponse('Hello World!')