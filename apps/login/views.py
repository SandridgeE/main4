from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from .models import User
from django.contrib import messages

def flash_errors(errors, request):
	for error in errors:
		messages.error(request, error)

def loginscreen(request):

	return render(request, 'login/loginscreen.html')

def success(request):
	return render(request, 'login/success.html')

def register(request):
	errors = User.objects.validate_registration(request.POST)
	if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			return redirect('/')


	User.objects.create(
		first_name = request.POST['first_name'],
		last_name = request.POST['last_name'],
		email = request.POST['email'],
		password = request.POST['password'],
		#address = request.POST['address'],
		#credit_card = request.POST['credit_card']
		)
	
	return redirect(reverse('landing'))

def login(request):
	pass
# Create your views here.
