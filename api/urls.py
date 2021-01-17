from django.urls import path
from .views import *

urlpatterns = [
    # path('flights/',Flights.as_view()), 
    path('flights/', flight),
    path('hello/',Hello.as_view()), #test
    # path('flights/<int:f_id>/', FlightUpdate.as_view()),
    path('flights/<int:f_id>/',updateFlight),
]