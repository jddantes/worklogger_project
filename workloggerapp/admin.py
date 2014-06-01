from django.contrib import admin
from workloggerapp.models import Project, Log
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
	list_display= ('name', 'total_hours')

admin.site.register(Project, ProjectAdmin)

class LogAdmin(admin.ModelAdmin):
	list_display = ('project', 'duration', 'remarks', 'user', 'date',)

admin.site.register(Log, LogAdmin)