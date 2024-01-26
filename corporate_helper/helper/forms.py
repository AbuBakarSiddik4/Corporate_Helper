
from django import forms
from django.forms import ModelForm
from .models import Employee,Device,DeviceLog

# The CreateEmployeeForm class is a ModelForm that is used to create a new Employee object, with all
# fields except the 'company' field included.
class CreateEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['company']

# The CreateDeviceForm class is a ModelForm that is used to create a new Device object with all fields
# included.
class CreateDeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = '__all__'


# The `CreateDeviceLogForm` class is a ModelForm that is used to create a form for the `DeviceLog`
# model with all fields and specific widgets for the 'given' and 'returned' fields.
class CreateDeviceLogForm(ModelForm):
    class Meta:
        model = DeviceLog
        fields = '__all__'
        widgets = {
            'given': forms.DateInput(attrs={'type': 'date'}),
            'returned': forms.DateInput(attrs={'type': 'date'}),
        }
