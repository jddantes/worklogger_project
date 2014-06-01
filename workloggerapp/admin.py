from django.contrib import admin
from workloggerapp.models import Project, Log
# Register your models here.

admin.site.register(Project)

admin.site.register(Log)