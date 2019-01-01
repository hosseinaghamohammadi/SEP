from django.urls import path

from . import views

urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('SignIn/', views.sign_in, name='Sign In'),
    path('workSeeker/', views.work_seeker, name='workseeker page'),
]