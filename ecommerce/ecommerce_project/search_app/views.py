from django.shortcuts import render
from ecommerce_app.models import product
from django.db.models import Q


# Create your views here.

def search_result(request):
    query = None
    prod = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        print(query)
        prod = product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))

        return render(request, 'search.html', {'query': query, 'product': prod})
