from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Flight(models.Model):
    flight_id = models.CharField(validators=[RegexValidator(regex='[A-Z]{2}[0-9]{4}')], max_length=6)
    date = models.CharField(validators=[RegexValidator(regex='[0-9]{2}\/[0-9]{2}\/[0-9]{4}')], max_length=10)
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    phone = models.CharField(validators=[RegexValidator(regex='[0-9]{10}')], max_length=10)

    def __str__(self):
        return self.flight_id + " " + self.date

    # class Meta:
    #     fields = ('flight_id', 'date', 'source', 'destination', 'phone')