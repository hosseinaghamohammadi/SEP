from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path

urlpatterns = [
    path('',lambda x:redirect('website/')),
    path('website/', include('website.urls')),
    path('admin/', admin.site.urls),
]