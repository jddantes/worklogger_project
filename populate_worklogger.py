import os

def populate():
	user = add_user(username='user', password='password')
	user2 = add_user(username='user2', password='password2')

	project1 = add_project(name='Project 1')
	project2 = add_project(name='Save the Earth')
	project3 = add_project(name='Cool project')

	add_log(user=user, duration=2, remarks='Remark etc etc', project=project1)

	add_log(user=user, duration=3, remarks='I saved the earth!', project=project2)
	add_log(user=user, duration=2, remarks='Saved the earth once more', project=project2)

	add_log(user=user, duration=1, remarks="I'm cool", project=project3)
	add_log(user=user, duration=2, remarks="I'm still cool", project=project3)

	add_log(user=user2, duration=5, remarks="NOPE I'M COOLER", project=project3)
	add_log(user=user2, duration=6, remarks="SAVE THE EARTH", project=project2)
	add_log(user=user2, duration=3, remarks="YOU'RE WELCOME MOTHER EARTH", project=project2)

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
	u.set_password(password)
	u.save()
	# print("Password "+password+" hashed to "+u.password)
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
	print("Date: "+log.date.strftime("%m %d %Y"))
	print("Date logged: "+log.date_logged.strftime("%m %d %Y"))
	print("")

# Start execution here!

if __name__ == '__main__':
	print ("Starting Worklogger population script...")
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'worklogger_project.settings')
	from workloggerapp.models import Project, Log
	from django.contrib.auth.models import User
	from django import forms
	import datetime
	from time import *
	populate()