from django.db.models.lookups import LessThan
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.shortcuts import render


# Create your views here.
from market.forms import ProductForm
from market.models import CATEGORY, Product


def index_view(request,):
    products = Product.objects.filter(balance__gte=1)
    products = products.order_by("categories", "name")
    context = {"products": products}
    return render(request, "index.html", context)

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product.html", {"product": product})

def create(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, "create.html", {"form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            balance = form.cleaned_data.get("balance")
            price = form.cleaned_data.get("price")
            new_product = Product.objects.create(name=name, balance=balance, price=price )
            return redirect("index_view", )
        return render(request, "create.html", {"form": form})



