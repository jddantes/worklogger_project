import os

def populate():
	user = add_user(username='user', password='password')
	project1 = add_project(name='Project 1')
	project2 = add_project(name='Save the Earth')

	add_log(user=user, duration=2, remarks='Remark etc etc', project=project1)
	add_log(user=user, duration=3, remarks='I saved the earth!', project=project2)

	# Print users
	print("Users:")
	for user in User.objects.all():
		print("[+] Username: " + user.username)
	print("")

	# Print projects
	print("Projects:")
	for project in Project.objects.all():
		print("[+] Project Name: " + project.name)
	print("")

	# Print Logs
	print("Logs:")
	for log in Log.objects.all():
		printlog(log)


def add_user(username, password):
	u = User.objects.get_or_create(username=username, password=password)[0]
	return u

def add_project(name):
	p = Project.objects.get_or_create(name=name)[0]
	return p

def add_log(user, duration, remarks, project):
	l = Log.objects.get_or_create(user=user, duration=duration, remarks=remarks, project=project)[0]

def printlog(log):
	print("[+] Log:")
	print("Project: "+log.project.name)
	print("Duration: "+str(log.duration))
	print("Remarks: "+log.remarks)
	print("User: "+log.user.username)
	print("Date "+log.date.strftime("%m %d %Y"))
	print("")

# Start execution here!

if __name__ == '__main__':
	print ("Starting Worklogger population script...")
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'worklogger_project.settings')
	from workloggerapp.models import Project, Log
	from django.contrib.auth.models import User
	import datetime
	from time import *
	populate()