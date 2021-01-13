from django.urls import path
from .views import all_flights, hello

urlpatterns = [
    path('all-flights/',all_flights),
    path('hello/',hello),
]