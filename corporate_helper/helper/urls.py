
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.loginPage,name='login'),
    path('logout/', views.logoutPage,name='logout'),
    path('register/', views.registrationPage,name='register'),
    path('add-employee/', views.addEmployee,name='add-employee'), 
    path('all-employee/', views.allEmployee,name='all-employee'), 
    path('delete/<str:pk>/', views.deleteEmployee,name='delete'), 
    path('add-device/', views.addDevice,name='add-device'), 
    path('add-device-log/', views.addDeviceLog,name='add-device-log'), 
]