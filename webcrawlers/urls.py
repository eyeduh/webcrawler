from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brands-list/', views.list_brands, name='brands-list'),
    path('products-list/', views.list_products, name='products-list'),
    path('brands-list/brand-products/',  views.brand_products, name='brand-products')

]