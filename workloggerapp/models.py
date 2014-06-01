from django.db import models
from django.contrib.auth.models import User
import datetime
from time import *
# Create your models here.

class Project(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class Log(models.Model):
	project = models.ForeignKey(Project)
	duration = models.IntegerField()
	remarks = models.CharField(max_length=128)
	user = models.ForeignKey(User)
	date = models.DateField( default=datetime.date.today)


	def __str__(self):
		#return u'%s - %s - %s' % (self.project, self.date|date:"M d Y",self.remarks)
		return str(self.project.name + self.date.strftime('%m %d %Y') + self.remarks)
