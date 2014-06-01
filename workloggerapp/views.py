from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from workloggerapp.models import Log, Project
from django.db.models import Sum
import datetime
from time import *

# Create your views here.

@login_required
def index(request):
	context = RequestContext(request)
	context_dict = {}
	user = request.user

	log_list = Log.objects.filter(user__username=user.username)
	context_dict['log_list'] = log_list

	today = datetime.date.today()
	start_week = today - datetime.timedelta(today.weekday())
	end_week = start_week + datetime.timedelta(7)

	logs_today = Log.objects.filter(user__username=user.username, date=today).aggregate(Sum('duration'))['duration__sum']
	context_dict['logs_today'] = logs_today

	logs_thisweek = Log.objects.filter(user__username=user.username, date__range=[start_week, end_week]).aggregate(Sum('duration'))['duration__sum']
	context_dict['logs_thisweek'] = logs_thisweek

	logs_thismonth = Log.objects.filter(user__username=user.username, date__month=today.month).aggregate(Sum('duration'))['duration__sum']
	context_dict['logs_thismonth'] = logs_thismonth

	return render_to_response('workloggerapp/index.html', context_dict, context)

def user_login(request):
	context = RequestContext(request)

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/workloggerapp/')
			else:
				return HttpResponse("Your Rango account is disabled")
		else :
			print ("Invalid login deetails: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied")
	else:
		return render_to_response('workloggerapp/login.html', {}, context)

@login_required
def user_logout(request):
	context = RequestContext(request)
	logout(request)
	return HttpResponseRedirect('/workloggerapp/')
