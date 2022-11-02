from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(vehicle)
admin.site.register(car)
admin.site.register(Truck)
admin.site.register(Student)
admin.site.register(dept)
admin.site.register(club)
admin.site.register(access)

@admin.register(customer)
class paymentadmin(admin.ModelAdmin):
    list_display = ('name','amount')
