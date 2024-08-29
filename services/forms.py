# services/forms.py

from django import forms
from .models import Service
from users.models import RequestedService

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'field', 'price_per_hour']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['field'].widget = forms.Select(choices=Service.FIELD_CHOICES)

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = RequestedService
        fields = ['address', 'service_time']
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Enter service address'}),
            'service_time': forms.NumberInput(attrs={'min': 1, 'max': 24})
        }