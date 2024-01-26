from django.shortcuts import render,redirect
from .forms import CreateEmployeeForm,CreateDeviceForm,CreateDeviceLogForm
from .models import Employee,Device,DeviceLog
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.



def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request,"SignUp First.")
        user = authenticate(request, username=user.username, password=password)
        print('user' , user)
        if user is not None:
            login(request,user)
            # return redirect('index')
        else:
            messages.error(request,"Username or Password Not Found")
    context = {'page':page}
    return render(request,'helper/login_register.html',context)

def logoutPage(request):
    logout(request)
    return redirect('index')

def registrationPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        existing_user = User.objects.filter(email=email).exists()
        if not existing_user:
            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')
        else:
            messages.error(request, "User with this email already exists.")
    context = {}
    return render(request,'helper/login_register.html',context)

def index(request):
    device_log = DeviceLog.objects.all()
    context = {"device_log": device_log,}
    return render(request,'helper/index.html',context)

def addEmployee(request):
    form = CreateEmployeeForm()
    if request.method == 'POST':
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.company = request.user
            employee.save()
            return redirect('index')
    context = {'form':form}
    return render(request,'helper/form.html',context)

def addDevice(request):
    form = CreateDeviceForm()
    if request.method == 'POST':
        form = CreateDeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request,'helper/form.html',context)



def addDeviceLog(request):
    form = CreateDeviceLogForm()
    if request.method == 'POST':
        form = CreateDeviceLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request,'helper/form.html',context)