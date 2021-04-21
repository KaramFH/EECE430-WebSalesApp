from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def home(request): #home page
	return render(request, 'store/home.html')

def about(request): #about page
	return render(request, 'store/about.html')

def products(request): #products page

	context = {
		'products' : Product.objects.all()
	}	

	return render(request,'store/products.html',context)

def contact(request): #contact page
	return HttpResponse('<h1>Store Contact</h1>')

# def account(request): #account page
# 	return HttpResponse('<h1>Store Account</h1>')

