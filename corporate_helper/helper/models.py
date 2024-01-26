from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    company = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name    

class Device(models.Model):
    category = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.category

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)    
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)  
    check_out = models.DateTimeField(auto_now=False, null=True)
    check_in = models.DateTimeField(auto_now=False, null=True)
    check_out_condition = models.CharField(max_length=50)
    check_in_condition = models.CharField(max_length=50)
    def __str__(self):
        return self.device.model   