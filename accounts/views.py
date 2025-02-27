# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Username taken')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request, 'Email taken')
				return redirect('register')
			else:
				user = User.objects.create_user(
					username =username,
					first_name = first_name,
					last_name = last_name, 
					email = email,
					password = password1,
					)
				user.save()
				return redirect('create_profile')
		else:
			messages.info(request, 'Password not matching')
			return redirect('register')

	else:
		return render(request, 'register.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('index')
		else:
			messages.info(request, 'Invalid Username and password')
			return redirect('login')

	return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return redirect('login')


# Create your views here.
