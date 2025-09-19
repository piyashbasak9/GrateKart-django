from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'slug', 'price', 'stock', 'is_available', 'category', 'created_date', 'modified_date')
    prepopulated_fields = {'slug': ('product_name',)}
    search_fields = ('product_name',)
    list_filter = ('is_available', 'category', 'created_date', 'modified_date')

admin.site.register(Product, ProductAdmin)
