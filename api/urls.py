from django.urls import path
from .views import *

urlpatterns = [
    path('all-flights/',all_flights), # GET request to retrieve all data
    path('hello/',hello), #test
    path('book-flight/',book_flight)
]