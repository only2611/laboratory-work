from django.db.models.lookups import LessThan
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.shortcuts import render


# Create your views here.

from market.models import CATEGORY, Product


def index_view(request,):
    products = Product.objects.filter(balance__gte=1)
    products = products.order_by("categories", "name")
    context = {"products": products}
    return render(request, "index.html", context)

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product.html", {"product": product})

