from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Category, Brand, Product

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list_brands(request):
    brands = Brand.objects.all()
    context = {'brands' : brands}
    return render(request, 'list_brands.html', context)

def list_products(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'list_products.html', context)

def brand_products(request):
    products = Product.objects.all()
    brands = Brand.objects.all()
    context = {'products' : products, 'brands' : brands}
    return render(request, 'brand-products.html', context)