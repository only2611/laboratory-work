

from django.urls import path

from market.views import index_view, create, update_product, delete
from market.views import product_view


urlpatterns = [
    path("", index_view, name="index_view"),
    path('product/<int:pk>/', product_view, name="product_view"),
    path('create/', create, name="create"),
    path('product/<int:pk>/update', update_product, name="update_product"),
    path('product/<int:pk>/delete', delete, name="delete"),
]