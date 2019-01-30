from django.urls import path

from . import views

urlpatterns = [
    path('', views.global_homepage, name='global homepage'),
    path('SignInEmployee/', views.sign_in_employee, name='Employee Sign In'),
    path('SignInEmployer/', views.sign_in_employer, name='Employer Sign In'),
    path('<int:employee_id>/employee/', views.employee, name='employee page'),
    path('<int:employer_id>/employer/', views.employer_temp, name='employer page'),
    path('employee/', views.employee_temp, name='employee profile'),
    path('employer/', views.employer_temp, name='employer profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('employee_home/', views.employee_home, name='employee homepage')
]
