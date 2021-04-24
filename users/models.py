from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)

	firstname = models.TextField()
	lastname = models.TextField()
	dateofbirth = models.DateField()
	phonenumber =  models.TextField()
	province =  models.TextField()
	city =  models.TextField()
	addresss =  models.TextField()

	def __str__(self):
		return f'{self.firstname} {self.lastname}'