from django.db import models

# Create your models here.
class Flights(models.Model):
    flight_id = models.CharField(max_length=6)
    date = models.CharField(max_length=10)
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    phone = models.PositiveBigIntegerField()
    