from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    description = models.TextField(default='My first product ever!')
