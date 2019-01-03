from django.urls import path

from . import views

urlpatterns = [
    path('', views.global_homepage, name='global homepage'),
    path('sign_in/', views.sign_in, name='sign in'),
    path('employee/', views.employee, name='employee homepage'),
    path('edit_profile/', views.edit_profile, name='edit_profile')
]