from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def register_user(request):
	print('get mai gaya')
	if request.method == 'POST':
		print('post mai gaya')
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You have registered in successfully...")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form': form})
	return render(request, 'register.html', {'form': form})

def home(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		#authenticate
		user = authenticate(request, username=username, password=password)
		
		if user is not None:
			login(request, user)
			messages.success(request, "You have been logged in successfully...")
			return redirect('home')
		else:
			messages.success(request, "There was an error logging in. Please try again later.")
			return redirect('home')
	else:
		return render(request, 'home.html',{})
	ret


def logout_user(request):
	logout(request)
	messages.success(request, "You have been logged out successfully...")
	return redirect('home')