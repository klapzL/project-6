from django_earthdistance.models import EarthDistanceQuerySet
from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(null=True, blank=True, upload_to='manufac_logos')

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag, verbose_name='Tags', related_name='products')

    def __str__(self):
        return self.model


class House(models.Model):
    lattitude = models.FloatField()
    longtitude = models.FloatField()
    objects = EarthDistanceQuerySet.as_manager()