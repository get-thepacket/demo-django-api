from django.urls import path
from .views import *

urlpatterns = [
    path('flights/',Flights.as_view()), 
    path('hello/',Hello.as_view()), #test
    path('flights/<int:f_id>/', FlightUpdate.as_view()),
]