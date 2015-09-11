from django import forms
from .models import Customer
from django.contrib.auth.models import User

class CustomerRegisterForm(forms.ModelForm):
	class Meta:
		model = Customer

class UserRegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'first_name', 'last_name']