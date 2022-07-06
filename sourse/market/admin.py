from django.contrib import admin

# Register your models here.

# Register your models here.
from market.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description', 'categories',]
    list_display_links = ['name']
    list_filter = ['categories']
    search_fields = ['categories', 'name']
    fields = ['name', 'description', 'categories', 'balance', 'price']


admin.site.register(Product, ProductAdmin)