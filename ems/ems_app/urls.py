from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home_page'),
    path('contact/', views.contact_us, name='contact_page'),
    
    path('login/', LoginView.as_view(template_name='ems_app/login.html'), name='login_page'),
    path('profile/', views.employee_profile, name='employee-profile'),
]
