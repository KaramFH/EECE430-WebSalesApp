from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from cart.cart import Cart
from django_mysql.models import ListTextField
from django.db.models import IntegerField, CharField, Model

class OrderSummary(models.Model):

	user = models.OneToOneField(User, on_delete = models.CASCADE)

	items = ListTextField(base_field = CharField(max_length = 255))

	def add_item(self,t):
		self.items.append(t)

	def __str__(self):
		return user
