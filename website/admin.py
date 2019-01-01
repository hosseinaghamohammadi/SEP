from django.contrib import admin

from .models import Employer, Phone, WorkSeeker, User

admin.site.register(User)
admin.site.register(Employer)
admin.site.register(WorkSeeker)
admin.site.register(Phone)