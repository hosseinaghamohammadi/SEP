from django.contrib import admin

from .models import Employer, Phone, WorkSeeker

admin.site.register(Employer)
admin.site.register(Phone)
admin.site.register(WorkSeeker)