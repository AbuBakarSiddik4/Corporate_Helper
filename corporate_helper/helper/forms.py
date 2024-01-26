
from django.forms import ModelForm
from .models import Company,Employee,Device,DeviceLog

class RegistrationFrom(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class LoginForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ['name']


class CreateEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['company']

class CreateDeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = '__all__'


class CreateDeviceLogForm(ModelForm):
    class Meta:
        model = Device
        fields = '__all__'
