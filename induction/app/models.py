import json

from django.db import models

class vehicle(models.Model):
    lp_number=models.CharField(max_length=20)
    wheel_count=models.IntegerField(null=True)
    manufacturer=models.CharField(max_length=30)
    model_name=models.CharField(max_length=30)
    class Meta:
        indexes=[models.Index(fields=['lp_number','manufacturer'])]
    def __str__(self):
        return self.model_name
class car(vehicle):
    has_roof_top=models.BooleanField(default=False)
    file=models.FileField(upload_to="media")
    def __str__(self):
        return self.model_name

class Truck(vehicle):

    max_goods_weight=models.DecimalField(max_digits=12,decimal_places=2)
    def __str__(self):
        return self.model_name


class dept(models.Model):
    branch=models.CharField(max_length=20,db_index=True)


    def __str__(self):
        return self.branch

class club(models.Model):
    title=models.CharField(max_length=30,db_index=True)

    def __str__(self):
        return self.title

class access(models.Model):
    accesscard=models.IntegerField(null=False)
    departmentaccess=models.ForeignKey(dept,on_delete=models.PROTECT)

class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    department=models.ForeignKey(dept,on_delete=models.PROTECT)                  #---------------many to one relation
    clubs=models.ManyToManyField(club)                                           #--------------many to many relation
    accesscard=models.OneToOneField(access,null=True,on_delete=models.SET_NULL)  #----------------one to one relation
    def __str__(self):
        return self.first_name+' '+self.last_name

class customer(models.Model):
    name=models.CharField(max_length=35)
    amount=models.IntegerField(null=False)

