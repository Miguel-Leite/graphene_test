from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Product(models.Model):
    product = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    price = models.FloatField(default=0.000)
    description = models.TextField()

    def __str__(self):
        return self.product
