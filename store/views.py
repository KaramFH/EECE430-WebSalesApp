from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def home(request): #home page
	return render(request, 'store/home.html')

def about(request): #about page
	return render(request, 'store/about.html')

def products(request): #products page

	sort = request.GET.get('sort', 'price') 
	
	context = {
		'products' : Product.objects.all().order_by(sort)
	}	


	return render(request,'store/products.html',context)

def contact(request): #contact page
	return render(request, 'store/contact.html')

# def account(request): #account page
# 	return HttpResponse('<h1>Store Account</h1>')

