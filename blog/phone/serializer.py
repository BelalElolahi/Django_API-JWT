from rest_framework import serializers

from .models import Phone


class PhoneSerializer(serializers.ModelSerializer):
    class Meta : 
        fields=['phone_name','phone_descrption','phone_id','owner']
        model=Phone