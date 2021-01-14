from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Flight
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Flights(View):
    def get(self, request):
        f = Flight.objects.all()
        count = Flight.objects.count()
        dict_data = serializers.serialize('python',f) # convert the QuerySet to Dictionary
        data = {
            "flights": dict_data,
            "flight_count": count
        }
        return JsonResponse(data)

    def post(self, request):
        body = json.loads(request.body)
        
        flight_id = body.get('flight_id')
        source = body.get('source')
        destination = body.get('destination')
        date = body.get('date')
        phone = body.get('phone')

        flight_data = {
            'flight_id': flight_id,
            'source': source,
            'destination': destination,
            'date': date,
            'phone': phone
        }

        obj = Flight.objects.create(**flight_data)
        response = {
            'message': f'New entry created with id {obj.id}',
            'id': obj.id
        }
        return JsonResponse(response)

@method_decorator(csrf_exempt, name='dispatch')
class FlightUpdate(View):
    #not working as of now
    def get(self, request, f_id):
        f = Flight.objects.get(id=f_id)
        dict_data = serializers.serialize('json',f) # convert the QuerySet to Dictionary
        response = {
            "data":dict_data
        }
        return JsonResponse(response)

    def put(self, request, f_id):
        flight = Flight.objects.get(id=f_id)

        body = json.loads(request.body)
        flight.date = body.get('date')
        flight.save()

        response = {
            'message': f'The flight with id {f_id} has been updated'
        }
        return JsonResponse(response)
    
    def delete(self, request, f_id):
        flight = Flight.objects.get(id=f_id)
        flight.delete()

        response = {
            'message': f'{f_id} has been deleted'
        }
        return JsonResponse(response)

class Hello(View):
    def get(self, request):
        return JsonResponse({"message":"This is a get request"})
    def post(self, request):
        return JsonResponse({'message':'This is a post request'})
    def put(self, request):
        return JsonResponse({'message':'This is a put request'})
    def delete(self, request):
        return JsonResponse({'message':'This is a delete request'})
    