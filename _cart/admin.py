from django.contrib import admin
from .models import OrderSummary
from django.utils.html import format_html
# Register your models here.


admin.site.register(OrderSummary)