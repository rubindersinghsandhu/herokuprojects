from rest_framework import serializers
from .models import predictor

class predictorSerializers(serializers.ModelSerializer):
    class Meta:
        model=predictor
        fiels='__all__'
