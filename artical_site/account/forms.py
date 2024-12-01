from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.TextInput()
	last_name = forms.TextInput()

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	first_name = forms.TextInput()
	last_name = forms.TextInput()

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['img']