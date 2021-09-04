from django.urls import path

from . import views

urlpatterns = [
    path('brands-list/', views.list_brands, name='brands-list'),
    path('brands-list/brand-products/', views.list_products, name='products-list'),

]