from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.db import models
from .models import Profile

# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created. Happy Shopping!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):

	user = models.OneToOneField(User, on_delete = models.CASCADE)

	profile = Profile.objects.all()

	context = {
		'profile':profile
	}


	return render(request,'users/profile.html',context)

def editprofile(request):
	return render(request,'users/editprofile.html')

