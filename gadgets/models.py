from distutils.command.upload import upload
from tokenize import blank_re
from unicodedata import category
from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(null=True, blank=True, upload_to='manufac_logos')

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateField

    def __str__(self):
        return self.model
