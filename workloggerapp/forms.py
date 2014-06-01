from django import forms
from workloggerapp.models import Project, Log
from django.contrib.auth.models import User
import datetime

class LogForm(forms.ModelForm):
	project = forms.ModelChoiceField(queryset=Project.objects.all(), to_field_name='name')
	duration = forms.DecimalField(max_digits=4, decimal_places=2)
	remarks = forms.CharField(max_length=128, initial='')
	date = forms.DateField(initial=datetime.date.today())
	date_logged = forms.DateField(initial=datetime.date.today(), widget=forms.HiddenInput())
	user = forms.ModelChoiceField(queryset=User.objects.all() )

	
	# Not working 
	#def __init__(self, user_object, user, *args, **kwargs):
		#print("Filler")
		# self.user = kwargs.pop('user', None)
		# super(LogForm, self).__init__(*args, **kwargs)
		# print("User is "+self.user.username) # Prints correctly
		# self.user = forms.ModelChoiceField(queryset=User.objects.all(), to_field_name='username', initial=User.objects.get(username='admin'))

	# Workaround: 
	# Get user.id in views.index and pass it as {{hard_user_id}}
	# Use {{hard_user_id}} to modify the select option values in index.html and hide the select itself with css

	class Meta:
		model = Log
		fields = ( 'duration', 'project', 'remarks', 'date', 'date_logged', 'user')

