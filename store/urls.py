from django.urls import path
from . import views

urlpatterns = [ #urls for the functions in views.py-store
    path('', views.home, name='store-home'),
    path('about/', views.about, name='store-about'),
    path('products/', views.products, name='store-products'),
    path('contact/', views.contact, name='store-contact'),
    # path('account/', views.account, name='store-account'),
]