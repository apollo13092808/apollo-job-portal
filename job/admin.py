from django.contrib import admin

from job.models import Applicant, Recruiter, Job

# Register your models here.
admin.site.register(Applicant)
admin.site.register(Recruiter)
admin.site.register(Job)
