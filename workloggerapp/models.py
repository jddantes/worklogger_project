from django.db import models
from django.contrib.auth.models import User
import datetime
from time import *
from django.db.models import Sum
# Create your models here.

class Project(models.Model):
	name = models.CharField(max_length=128)

	def total_hours(self):
		return Log.objects.filter(project=self).aggregate(Sum('duration'))['duration__sum']

	def __str__(self):
		return self.name

class Log(models.Model):
	project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
	duration = models.DecimalField(max_digits=4, decimal_places=2)
	remarks = models.CharField(max_length=128)
	user = models.ForeignKey(User)
	date = models.DateField( default=datetime.date.today)
	date_logged = models.DateField( auto_now_add=True)

	def __str__(self):
		#return u'%s - %s - %s' % (self.project, self.date|date:"M d Y",self.remarks)
		return str(self.project.name + " on " + self.date.strftime('%m %d %Y') + " by " + self.user.username)
