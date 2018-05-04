from django.shortcuts import render, redirect
from my_app.forms import RegistrationForm, EditProfileForm#We now can use this form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def home(request):
	context = {
		'title' : "Home page content and descriptions will be added soon"# тайтл це назва змінної і якщо ми вставим цю змінну в файд home.html Значення буде відображено
	}

	return render(request, 'my_app/home.html', context)

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
		form = EditProfileForm(request.POST, instance=request.user)#Для того щоб показувати інформацію коректно

		if form.is_valid():
			form.save()
			return redirect('/profile')

	else:
		form = EditProfileForm(instance=request.user)
		args = {'form': form}
		return render(request, 'my_app/edit_profile.html', args)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/profile')
		else:
			return redirect('/my_app/change_password')
	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form': form}
		return render(request, 'my_app/change_password.html', args)