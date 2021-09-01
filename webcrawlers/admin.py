from django.contrib import admin
from .models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    list_filter = ['name']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'url', 'img', 'price']
    list_filter = ['price']

admin.site.register(Product, ProductAdmin)

