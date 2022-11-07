from django.contrib import admin
from .models import *
from django.contrib.sessions.models import Session
# Register your models here.
admin.site.register(vehicle)
admin.site.register(car)
admin.site.register(Truck)
admin.site.register(Student)
admin.site.register(dept)
admin.site.register(club)
admin.site.register(access)
admin.site.register(Session)

@admin.register(customer)
class paymentadmin(admin.ModelAdmin):
    list_display = ('name','amount')
