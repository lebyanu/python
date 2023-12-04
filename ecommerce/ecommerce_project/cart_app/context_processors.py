from .models import cart_items, Cart
from .views import _cart_id
from django.core.exceptions import ObjectDoesNotExist

def item_counter(request):
    counter = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            crt = Cart.objects.filter(cart_id=_cart_id(request))
            crt_item = cart_items.objects.all().filter(cart=crt[:1])
            for c_item in crt_item:
                counter += c_item.quantity
        except Cart.DoesNotExist:
            counter=0
    return dict(counter=counter)

