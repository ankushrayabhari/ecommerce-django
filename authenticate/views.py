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
				return HttpResponse("Your account is disabled. <br> <a href='/'> Return to home page </a>")
		else:
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'authenticate/login.html')

@login_required
def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(reverse('main:index'))

def register(request):
	registered = False
	if request.method == 'POST':
		userForm = UserRegisterForm(data=request.POST)
		customerForm = CustomerRegisterForm(data=request.POST)

		if userForm.is_valid() and customerForm.is_valid():
			user = userForm.save()
			user.set_password(user.password)
			user.save()
			customer = customerForm.save(commit=False)
			customer.user = user
			customer.save()
			registered = True
		else:
			print(userForm.errors, customerForm.errors)

	else:
		userForm = UserRegisterForm()
		customerForm = CustomerRegisterForm()

	return render(request, 'authenticate/register.html', {'userForm': userForm, 'customerForm': customerForm, 'registered': registered})