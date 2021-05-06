from django.db import models
from django.contrib.auth.models import User
from store.models import Product

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)

	# items = models.ManyToManyField(Product, blank=True)

	firstname = models.TextField()
	lastname = models.TextField()
	dateofbirth = models.DateField()
	phonenumber =  models.TextField()
	province =  models.TextField()
	city =  models.TextField()
	addresss =  models.TextField()

	def __str__(self):
		return f'{self.firstname} {self.lastname}'