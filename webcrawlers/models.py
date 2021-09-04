from os import name
from django.db import models
from django.db.models.deletion import PROTECT


# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name= 'Category Name', max_length=30)
    url = models.URLField(verbose_name= 'Category Link', max_length=100)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        unique_together = ['name', 'url']
    

    
class Brand(models.Model):
    name = models.CharField(verbose_name= 'Brand Name', max_length=200)
    url = models.CharField(verbose_name= 'Brand Link', max_length=100)
    new = models.CharField(verbose_name='Is It New?', max_length=10)

    class Meta:
        db_table = 'brands'
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        unique_together = ['name', 'url', 'new']

    def __unicode__(self):
        return self.url
    


class Product(models.Model):
    name = models.CharField(verbose_name= 'Product Name', max_length=100)
    brand = models.CharField(verbose_name= 'Product Brand', max_length=50)
    url = models.URLField(verbose_name= 'Product URL', max_length=200)
    img = models.URLField(verbose_name= 'Product Image', max_length=200)
    price = models.CharField(verbose_name= 'Product Price', help_text='In Dollars', max_length=50)
    

    class Meta: 
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


