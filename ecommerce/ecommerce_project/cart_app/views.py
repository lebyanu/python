from django.shortcuts import render, redirect, get_object_or_404
from ecommerce_app.models import product
from .models import cart_items, Cart
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, prod_id):
    products = product.objects.get(id=prod_id)
    print(products)
    try:
        c = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        c = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        c.save(),
    try:
        cart_item = cart_items.objects.get(product=products, cart=c)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()

    except cart_items.DoesNotExist:
        cart_item = cart_items.objects.create(
            product=products,
            quantity=1,
            cart=c,
        )
        cart_item.save()
    return redirect('cart_app:cart_details')


def cart_details(request, total=0, counter=0, cart_item=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = cart_items.objects.filter(cart_id=cart, active=True)

        for cart_itm in cart_item:
            total += (cart_itm.product.price * cart_itm.quantity)
            counter += cart_itm.quantity
    except ObjectDoesNotExist:
        pass

    return render(request, 'cart.html', dict(cart_items=cart_item, counter=counter, total=total))

# minus product quantity fro  cat
def remove_cart_item(request, prod_id):
    crt = Cart.objects.get(cart_id=_cart_id(request))
    prod = get_object_or_404(product, id=prod_id)
    crt_items = cart_items.objects.get(product=prod, cart=crt)
    if crt_items.quantity > 1:
        crt_items.quantity -= 1
        crt_items.save()
    else:
        crt_items.delete()
    return redirect('cart_app:cart_details')

# remove one product completly from cart #
def delete_cart_item(request,prod_id):
    crt = Cart.objects.get(cart_id=_cart_id(request))
    prod = get_object_or_404(product, id=prod_id)
    crt_items = cart_items.objects.get(product=prod, cart=crt)
    crt_items.delete()
    return redirect('cart_app:cart_details')