from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# The Employee class represents an employee with a name, email, and a foreign key to a company.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    company = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name    

# The `Device` class is a model that represents a device with a category and description.
class Device(models.Model):
    category = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.category

# The `DeviceLog` class represents a log entry for a device given to an employee by a company,
# including information such as the device, employee, dates, and conditions.
class DeviceLog(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  
    givenDate = models.DateTimeField(auto_now=False, null=True)
    returnedDate = models.DateTimeField(auto_now=False, null=True)
    given_condition = models.CharField(max_length=100, default='Good')
    returned_condition = models.CharField(max_length=100, default='Good')
    def __str__(self):
        return self.device.model   