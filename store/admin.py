from django.contrib import admin
from .models import Product
from django.utils.html import format_html
# Register your models here.


admin.site.register(Product)

list_display = ('image_tag','description_tag' )

# admin.site.register(
#     Product,
#     list_display=["image_tag"],
# )