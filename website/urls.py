from django.urls import path

from . import views

urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('SignInWorkseeker/', views.sign_in_workseeker, name='Workseeker Sign In'),
    path('SignInEmployer/', views.sign_in_employer, name='Employer Sign In'),
    path('workSeeker/', views.work_seeker, name='workseeker page'),
]