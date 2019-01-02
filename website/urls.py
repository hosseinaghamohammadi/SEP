from django.urls import path

from . import views

urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('SignIn/', views.sign_in, name='Sign In'),
    path('employee/', views.employee, name='workseeker page'),
    path('edit_profile/', views.edit_profile, name='edit_profile')
]