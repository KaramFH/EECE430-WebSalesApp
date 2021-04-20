from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
	title = models.CharField(max_length = 100)
	description = models.TextField()
	price = models.IntegerField()
	amount = models.IntegerField()
	picture = models.ImageField()
	item_number = models.TextField()
	barcode = models.TextField()


class Customer(models.Model):
	firstname = models.TextField()
	lastname = models.TextField()
	dateofbirth = models.DateField()
	phonenumber =  models.TextField()
	email = models.EmailField()
	province =  models.TextField()
	city =  models.TextField()
	addresss =  models.TextField()



