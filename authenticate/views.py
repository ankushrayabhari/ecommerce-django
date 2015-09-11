from django.shortcuts import *
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)

		if user:
			if user.is_active:
				auth.login(request, user)
				return HttpResponseRedirect(reverse('main:index'))
			else:
				return render(request, 'authenticate/login.html', {'message': "Your account has been disabled."})
		else:
			return render(request, 'authenticate/login.html', {'message': "Invalid username or password."})
	else:
		return render(request, 'authenticate/login.html')

@login_required
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(reverse('main:index'))

def register(request):
	if request.method == 'POST':
		userForm = UserRegisterForm(data=request.POST)

		if userForm.is_valid():
			u = userForm.save()
			u.set_password(user.password)
			u.save()
			customer = Customer(user = u)
			customer.save()
			return render(request, 'authenticate/login.html')
		else:
			print(userForm.errors)

	else:
		userForm = UserRegisterForm()

	return render(request, 'authenticate/register.html', {'userForm': userForm})