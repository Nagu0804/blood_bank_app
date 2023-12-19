from django import forms
from .models import Donor

class DonorSearch(forms.Form):
    class Meta:
        model = Donor
        fields = '__all__'
        widgets = {
            'location': forms.Select(attrs={'class': 'form-control', 'required': 'True'}),
            'blood_group': forms.Select(attrs={'class': 'form-control', 'required': 'True'}),
        }