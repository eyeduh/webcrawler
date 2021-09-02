from django.db import models
from scraper.spiders.category_crawler import CategorySpider
from scraper.spiders.product_crawler import ProductsSpider


# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name= 'Category Name', max_length=30)
    url = models.URLField(verbose_name= 'Category Link', max_length=100)
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name= 'Product Name', max_length=100)
    brand = models.CharField(verbose_name= 'Product Brand', max_length=100)
    url = models.URLField(verbose_name= 'Product URL', max_length=100)
    img = models.URLField(verbose_name= 'Product Image', max_length=200)
    price = models.IntegerField(verbose_name= 'Product Price', help_text='In Dollars')
    

    class Meta: 
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

category_dict = CategorySpider.__str__

