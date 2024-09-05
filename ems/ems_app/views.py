from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

# Create your views here.
def home(request):
    employees = [
        {'name': 'Alice Johnson', 
         'position': 'Nurse',
         'department': 'Emergency'},

        {'name': 'Bob Smith',
        'position': 'Doctor',
        'department': 'Cardiology'},

        {'name': 'Cathy Brown', 
         'position': 'Technician', 
         'department': 'Radiology'},
    ]
    return render(request,  'ems_app/home.html', {'employees': employees})

def contact_us(request):
    return render(request,  'ems_app/contact_us.html')

class EmployeeLoginView(LoginView):
    template_name = 'ems_app/login.html'

@login_required
def employee_profile(request):
    return render(request, 'ems_app/profile.html', {'username': request.user.username})