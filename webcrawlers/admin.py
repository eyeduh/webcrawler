from django.contrib import admin
from .models import Brand, Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    list_filter = ['name']

admin.site.register(Category, CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'new']
    list_filter = ['name']

admin.site.register(Brand, BrandAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'url', 'img', 'price']
    list_filter = ['brand']

admin.site.register(Product, ProductAdmin)

