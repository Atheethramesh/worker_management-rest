from rest_framework import serializers
from .models import Emp
from django.contrib.auth.models import User

class SignUpSer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=["first_name","last_name","email","username","password"]
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data) 
    
class Emps(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields="__all__"
        
