from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def index(request):
	context = RequestContext(request)

	return render_to_response('workloggerapp/index.html', {}, context)

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
