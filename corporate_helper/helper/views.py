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
    """
    The `loginPage` function handles the login functionality, checking if the user is authenticated,
    validating the login credentials, and redirecting the user to the index page if the login is
    successful.
    
    :param request: The `request` parameter is an object that represents the HTTP request made by the
    user. It contains information about the request, such as the user's browser, the requested URL, any
    submitted form data, and more
    :return: a rendered HTML template called 'login_register.html' with the context variable 'page'
    passed to it.
    """
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
            return redirect('index')
        else:
            messages.error(request,"Username or Password Not Found")
    context = {'page':page}
    return render(request,'helper/login_register.html',context)

def logoutPage(request):
    """
    The function logs out the user and redirects them to the index page.
    
    :param request: The request object represents the HTTP request that the user made to access the
    page. It contains information such as the user's session, cookies, and any data submitted in the
    request
    :return: a redirect to the 'index' page.
    """
    logout(request)
    return redirect('index')

def registrationPage(request):
    """
    The `registrationPage` function handles the registration process for a user, checking if the user is
    already authenticated, creating a new user if they don't exist, and displaying error messages if
    necessary.
    
    :param request: The `request` parameter is an object that represents the HTTP request made by the
    user. It contains information about the request, such as the user's session, the HTTP method used
    (GET, POST, etc.), and any data sent with the request
    :return: The function `registrationPage` returns a rendered HTML template called
    'helper/login_register.html' with an empty context dictionary if the request method is not POST or
    if the user is already authenticated. If the request method is POST and the user does not already
    exist, a new user is created with the provided username, email, and password, and the user is
    redirected to the 'login' page. If
    """
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

@login_required(login_url='/login')
def index(request):
    """
    This function returns the index page with device logs filtered by the company of the logged-in user.
    
    :param request: The request object represents the HTTP request that the user made. It contains
    information about the user, the requested URL, any submitted data, and other metadata
    :return: a rendered HTML template called 'index.html' with the context variable 'device_log' passed
    to it.
    """
    company = request.user.id
    device_log = DeviceLog.objects.filter(company=company)
    context = {"device_log": device_log,}
    return render(request,'helper/index.html',context)

def addEmployee(request):
    """
    The function `addEmployee` is used to handle a form submission for creating a new employee and
    saving it to the database.
    
    :param request: The `request` parameter is an object that represents the HTTP request made by the
    user. It contains information about the request, such as the method used (GET or POST), the user
    making the request, the data sent with the request, and more. In this code snippet, the `request`
    :return: a rendered HTML template called 'form.html' with the context variable containing the form.
    """
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

@login_required(login_url='/login')
def allEmployee(request):
    """
    This function retrieves all employees belonging to the company of the logged-in user and renders
    them in an HTML template.
    
    :param request: The request object represents the HTTP request made by the user. It contains
    information such as the user's session, the HTTP method used (GET, POST, etc.), and any data sent
    with the request
    :return: a rendered HTML template called 'employees.html' with a context variable containing a
    queryset of employees.
    """
    company = request.user.id
    employees = Employee.objects.filter(company=company)
    context = {'employees':employees}
    return render(request,'helper/employees.html',context)

def deleteEmployee(request,pk):
    """
    The function `deleteEmployee` deletes an employee object from the database and redirects to the
    index page.
    
    :param request: The request object represents the HTTP request that the user made to the server. It
    contains information such as the user's browser details, the requested URL, and any data sent with
    the request
    :param pk: The "pk" parameter stands for "primary key" and is used to identify a specific employee
    in the database. It is typically an integer value that uniquely identifies each employee record. In
    this case, it is used to retrieve the employee object from the database using the Employee model's
    "get" method
    :return: a redirect to the 'index' page if the request method is POST and the employee is
    successfully deleted. Otherwise, it is rendering the 'delete.html' template with the employee
    object.
    """
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('index')
    return render (request,'helper/delete.html',{'obj':employee})


def addDevice(request):
    """
    The function `addDevice` is used to handle a form submission for creating a new device, saving the
    form data if it is valid and redirecting to the index page.
    
    :param request: The `request` parameter is an object that represents the HTTP request made by the
    client. It contains information such as the request method (GET, POST, etc.), the request headers,
    the request body, and other relevant information
    :return: a rendered HTML template called 'form.html' with the context variable containing the form.
    """
    form = CreateDeviceForm()
    if request.method == 'POST':
        form = CreateDeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request,'helper/form.html',context)

def addDeviceLog(request):
    """
    The function `addDeviceLog` is used to handle a form submission for creating a device log entry and
    redirecting to the index page if the form is valid.
    
    :param request: The `request` parameter is an object that represents the HTTP request made by the
    client. It contains information such as the HTTP method used (GET, POST, etc.), the headers, the
    user's session, and the data sent in the request
    :return: a rendered HTML template called 'form.html' with the context variable containing the form.
    """
    form = CreateDeviceLogForm()
    if request.method == 'POST':
        form = CreateDeviceLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request,'helper/form.html',context)