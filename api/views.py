from django.shortcuts import render
# from django.core import serializers
# from django.http import HttpResponse, JsonResponse
from .models import Flight
# from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from .serializer import FlightSerializer

# Create your views here.

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all().order_by('date')
    serializer_class = FlightSerializer