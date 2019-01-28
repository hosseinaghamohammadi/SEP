from django.urls import path

from . import views

urlpatterns = [
    path('', views.global_homepage, name='global homepage'),
    path('sign_in/', views.sign_in, name='sign in'),
    path('employee/', views.employee, name='employee profile'),
    path('employer/', views.employer, name='employer profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('employee_home/', views.employee_home, name='employee homepage')
]