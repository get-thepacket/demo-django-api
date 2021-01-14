from rest_framework import serializers
from .models import Flight

class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flight
        fields = ('id','flight_id','date','source','destination','phone')