from . models import *
from rest_framework import serializers

class DestSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(required=False)

    class Meta:
        model=Destinations
        fields='__all__'
