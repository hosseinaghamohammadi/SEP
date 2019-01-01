from django.urls import path

from . import views

urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('signIn/', views.sign_in, name='Sign In'),
]