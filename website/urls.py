from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/employer/', views.EmployerSignUpView.as_view(), name='employer_signup'),
    path('accounts/signup/employee/', views.EmployeeSignUpView.as_view(), name='employee_signup'),
    path('signup/',views.signup),
    path('logout/',auth_views.LogoutView.as_view(template_name='website/global_homepage.html')),
    path('login/',auth_views.LoginView.as_view(template_name='website/login.html'),name='login'),
    path('', views.global_homepage, name='global homepage'),
    path('SignInEmployee/', views.sign_in_employee, name='Employee Sign In'),
    path('SignInEmployer/', views.sign_in_employer, name='Employer Sign In'),
    path('<int:employee_id>/employee/', views.employee, name='employee page'),
    path('<int:employer_id>/employer/', views.employer, name='employer page'),
    path('employee/', views.employee_temp, name='employee profile'),
    path('employer/', views.employer_temp, name='employer profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('employee_home/', views.employee_home, name='employee homepage'),
    path('getMail/<int:type>/<str:stdid>', views.get_mail, name='get mail'),
    path('verifyMail/<int:type>/<str:stdid>', views.verify_mail, name='verify mail'),
    path('fillFormEmployee/<str:mail>/<str:stdid>', views.fill_form_employee, name='fill form employee'),
    path('fillFormEmployer/<str:mail>', views.fill_form_employer, name='fill form employer'),
    path('verifyFormEmployee/<str:mail>/<str:stdid>', views.verify_form_employee, name='verify form employee'),
    path('verifyFormEmployer/<str:mail>/', views.verify_form_employer, name='verify form employer'),
    path('SignUpEmployee/', views.sign_up_employee, name='Sign Up Employee'),
    path('<int:employee_id>/employee/get_pdf', views.get_pdf, name='employee CV'),
    path('<int:employee_id>/employee/delete_experience/<int:experience_pk>', views.delete_experience,
         name='delete experience'),
    path('<int:employee_id>/employee/edit_experience/<int:experience_pk>', views.edit_experience,
         name='edit experience'),
    path('<int:employee_id>/employee/add_experience/', views.add_experience,
         name='add experience'),

    path('employee/<str:employee_name>', views.employee_profile_temp, name='employee profile temp'),


    path('searchPage/<int:employer_id>', views.search_page, name='search page'),

    path('<int:employer_id>/employer/delete_off/<int:empoff_pk>', views.delete_off,
         name='delete off'),
    path('<int:employer_id>/employer/edit_off/<int:empoff_pk>', views.edit_off,
         name='edit off'),
    path('<int:employer_id>/employer/add_off/', views.add_off,
         name='add off'),
    path('<int:employer_id>/employer/rate_off/<int:empoff_pk>', views.rate_off,
         name='rate off'),

]
