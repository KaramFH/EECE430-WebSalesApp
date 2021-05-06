from django.shortcuts import render, redirect
from store.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import OrderSummary


@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("store-products")


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

@login_required
def cart_detail(request):

    return render(request, '_cart/cart_detail.html')


# def order_summary(request):
#     cart = Cart(request)

#     for key,value in cart.cart.items():
#         print(value['name'])
#         # OrderSummary.add_item(value['name'])


#     return redirect("cart_clear")














