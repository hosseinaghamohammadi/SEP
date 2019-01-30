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
    path('employee_home/', views.employee_home, name='employee homepage'),
    path('getMail/<int:type>/', views.get_mail, name='get mail'),
    path('verifyMail/<int:type>/', views.verify_mail, name='verify mail'),
    path('fillFormEmployee/<str:mail>', views.fill_form_employee, name='fill form employee'),
    path('fillFormEmployer/<str:mail>', views.fill_form_employer, name='fill form employer'),
    path('verifyFormEmployee/<str:mail>/', views.verify_form_employee, name='verify form employee'),
    path('verifyFormEmployer/<str:mail>/', views.verify_form_employer, name='verify form employer'),
    path('SignUpEmployee/', views.sign_up_employee, name='Sign Up Employee'),
]
