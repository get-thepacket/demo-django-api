from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import View
from .models import Flight
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import FlightForm

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

def flight(request):
    obj = Flight()
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            obj.flight_id = form.cleaned_data.get('flight_id')
            obj.source = form.cleaned_data.get('source')
            obj.destination = form.cleaned_data.get('destination')
            obj.date = form.cleaned_data.get('date')
            obj.phone = form.cleaned_data.get('phone')

            obj.save()

            return HttpResponseRedirect('/flights/')

    f = Flight.objects.all()
    count = Flight.objects.count()
    dict_data = serializers.serialize('python',f) # convert the QuerySet to Dictionary
    
    return render(request, "flights.html", {'flights':dict_data, 'form':FlightForm})

def updateFlight(request, f_id):
    if request.method == "GET":
        f = Flight.objects.filter(id=f_id)
        dict_data = serializers.serialize('python',f)
        return render(request, "single_flight.html", {'flight':dict_data[0], 'form':FlightForm})
    if request.method == "POST":
        form = FlightForm(request.POST)
        # print(json.loads(request.body))
        if form.is_valid():
            obj = Flight.objects.get(id=f_id)
            print(form.cleaned_data)
            if form.cleaned_data.get('flight_id') != "":
                obj.flight_id = form.cleaned_data.get('flight_id')
            if form.cleaned_data.get('source') != "":
                obj.source = form.cleaned_data.get('source')
            if form.cleaned_data.get('destination') != "":
                obj.destination = form.cleaned_data.get('destination')
            if form.cleaned_data.get('date') != "":
                obj.date = form.cleaned_data.get('date')
            print(form.cleaned_data.get('phone'))
            if form.cleaned_data.get('phone') != 0:
                obj.phone = form.cleaned_data.get('phone')
            obj.save()
            return HttpResponseRedirect('/flights/'+str(f_id)+'/')

def deleteFlight(request, f_id):
    if request.method == "POST":
        flight = Flight.objects.get(id=f_id)
        flight.delete()
        return HttpResponseRedirect('/flights/')
    else:
        return HttpResponse('Invalid Request!')


@method_decorator(csrf_exempt, name='dispatch')
class FlightUpdate(View):
    
    def get(self, request, f_id):
        f = Flight.objects.filter(id=f_id)
        dict_data = serializers.serialize('python',f) # convert the QuerySet to Dictionary
        return JsonResponse(dict_data, safe=False)

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
    