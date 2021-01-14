from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_id = models.CharField(max_length=6)
    date = models.CharField(max_length=10)
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    phone = models.PositiveBigIntegerField()

    def __str__(self):
        return self.flight_id + " " + self.date

    # class Meta:
    #     fields = ('flight_id', 'date', 'source', 'destination', 'phone')