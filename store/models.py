from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class Product(models.Model):
	name = models.CharField(max_length = 255)
	description = models.TextField()
	price = models.FloatField()
	amount = models.IntegerField()
	image = models.ImageField(upload_to = 'product_pictures',default = '')
	item_number = models.TextField()
	barcode = models.TextField()

	def image_tag(self):
	    from django.utils.html import mark_safe
	    return mark_safe('<img src="%s" width="100px" height="100px" /><h2>%s - %s</h2>'%(self.image.url, self.name, self.item_number))
	image_tag.short_description = 'Image'

	def description_tag(self):
		from django.utils.html import mark_safe
		return mark_safe('<h3>%s</h3>'%(self.title))
	    
	description_tag.short_description = 'Description'

	def __str__(self):
		return self.image_tag()

	def add_product_to_cart(self):
		pass


		
# class Cart(models.Model):





