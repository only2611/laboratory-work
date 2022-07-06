

from django.urls import path

from market.views import index_view, create
from market.views import product_view


urlpatterns = [
    path("", index_view, name="index_view"),
    path('product/<int:pk>/', product_view, name="product_view"),
    path('create/', create, name="create"),
]