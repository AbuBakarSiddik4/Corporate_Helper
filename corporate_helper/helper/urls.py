
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.loginPage,name='login'),
    path('logout/', views.logoutPage,name='logout'),
    path('register/', views.registrationPage,name='register'),
    path('add-employee/', views.addEmployee,name='add-employee'), 
    path('add-device/', views.addDevice,name='add-device'), 
    path('add-device-log/', views.addDeviceLog,name='add-device-log'), 
]