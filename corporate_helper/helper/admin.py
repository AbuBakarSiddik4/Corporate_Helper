from django.contrib import admin
from .models import Employee,Device,DeviceLog
# Register your models here.

admin.site.register(Employee)
admin.site.register(Device)
admin.site.register(DeviceLog)