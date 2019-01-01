from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Employer)
admin.site.register(WorkSeeker)
admin.site.register(Phone)
admin.site.register(CV)
admin.site.register(SystemAdmin)
admin.site.register(JobOffer)
admin.site.register(JobRequest)
admin.site.register(Requirement)