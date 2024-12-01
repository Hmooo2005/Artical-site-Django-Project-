from django.shortcuts import render, redirect
from .forms import UserRegForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'User Have Created Successfuly Now You can Login!')
			return redirect('login')
	else:
		form = UserRegForm()
	return render(request, 'account/register.html', {'form': form})

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, 'Your Profile Have Updated Successfuly :)!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	context = {
		"u_form": u_form,
		"p_form": p_form,
	}
	return render(request, 'account/profile.html', context)