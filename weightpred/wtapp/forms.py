from django import forms
from .models import predictor
class weightform(forms.ModelForm):
    class Meta:
        model = predictor
        fields = '__all__'