from django_filters import rest_framework as filters
from .models import Student,vehicle

class Vehcilefilter(filters.FilterSet):

    class Meta:
        model=vehicle
        fields="__all__"