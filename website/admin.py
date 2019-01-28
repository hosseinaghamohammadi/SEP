from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Employer)
admin.site.register(Employee)
admin.site.register(Phone)
admin.site.register(CV)
admin.site.register(SystemAdmin)
admin.site.register(EmpOff)
admin.site.register(JobRequest)
admin.site.register(Requirement)