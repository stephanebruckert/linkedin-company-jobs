from django.contrib import admin
from jobs.models import Employer

class EmployerAdmin(admin.ModelAdmin):
    fields = ['name', 'description']

admin.site.register(Employer)

# Register your models here.
