from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    class Meta:
        model = Flight
        fields = '__all__'