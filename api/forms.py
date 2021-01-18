from django import forms
from .models import Flight
from django.utils.datastructures import MultiValueDict

class FlightForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        
    
    class Meta:
        model = Flight
        fields = '__all__'