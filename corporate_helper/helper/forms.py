
from django.forms import ModelForm
from .models import Employee,Device,DeviceLog

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
        model = DeviceLog
        fields = '__all__'
