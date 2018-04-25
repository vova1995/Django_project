from django.shortcuts import render, redirect
from my_app.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


def home(request):
	

	return render(request, 'my_app/home.html')

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/home')
	else:
		form = RegistrationForm()

		args = {'form': form}
		return render(request, 'my_app/reg_form.html', args)

def view_profile(request):
	args = {'user': request.user}
	return render(request, 'my_app/profile.html', args)

def edit_profile(request):
	if request.method == 'POST':
		form = UserChangeForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/profile')

	else:
		form = UserChangeForm(instance=request.user)
		args = {'form': form}
		return render(request, 'my_app/edit_profile.html', args)