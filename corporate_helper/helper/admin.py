from django.contrib import admin
from .models import Employee,Device,DeviceLog
# Register your models here.

# `admin.site.register(Employee)` is registering the `Employee` model with the Django admin site. This
# allows the `Employee` model to be managed and displayed in the admin interface.
admin.site.register(Employee)
admin.site.register(Device)
admin.site.register(DeviceLog)