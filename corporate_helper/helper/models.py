from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

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