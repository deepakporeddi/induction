from django import forms
from .models import *

class Vehicleform(forms.ModelForm):

    class Meta:
        model=vehicle
        fields="__all__"

class carform(forms.ModelForm):
    class Meta:
        model=car
        fields="__all__"

class Truckform(forms.ModelForm):
    class Meta:
        model=Truck
        fields="__all__"

class studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

class paymentform(forms.ModelForm):
    class Meta:
        model=customer
        fields="__all__"
    paid_to=forms.CharField(max_length=40)

