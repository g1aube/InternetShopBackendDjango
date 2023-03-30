from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=30)

class Product(models.Model):
    name = models.CharField(max_length=20, blank=False)
    category = models.ForeignKey(Category, blank=False, on_delete=models.CASCADE)

class ProductInfo(models.Model):
    quantity = models.PositiveIntegerField(blank=False)
    price = models.IntegerField()
    product = models.ForeignKey(Product, blank=False, on_delete=models.CASCADE)