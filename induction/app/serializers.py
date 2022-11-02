from rest_framework import serializers
from .models import *

class vehser(serializers.ModelSerializer):
    class Meta:
        model=vehicle
        fields='__all__'
class carser(serializers.ModelSerializer):
    class Meta:
        model=car
        fields='__all__'
class truser(serializers.ModelSerializer):
    class Meta:
        model=Truck
        fields='__all__'
class stuser(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"

class payser(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = "__all__"
class trsser(serializers.ModelSerializer):
    class Meta:
        model=customer
        fields="__all__"
class deptser(serializers.ModelSerializer):
    class Meta:
        model=dept
        fields='__all__'


