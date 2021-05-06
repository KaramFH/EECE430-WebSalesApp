from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

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
	return render(request,'users/profile.html')



# @login_required
# def view_orders(request):

# 	my_user_profile = Profile.objects.filter(user = request.user).first()

# 	my_orders = Order.objects.filter(is_ordered=True, owner= my_user_profile)

# 	context ={

# 		'my_orders': my_orders

# 	}

# 	return render(request, "_cart/cart_detail.html",context)