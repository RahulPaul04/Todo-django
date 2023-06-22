from rest_framework import serializers
from .models import items

class itemserializer(serializers.ModelSerializer):
    class Meta:
        model = items
        fields = ['id','name']