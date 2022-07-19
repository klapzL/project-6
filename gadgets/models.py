from tabnanny import verbose
from django_earthdistance.models import EarthDistanceQuerySet
from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(null=True, blank=True, upload_to='manufac_logos')

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    created_at = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag, verbose_name='Tags', related_name='products')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.model


class House(models.Model):
    lattitude = models.FloatField()
    longtitude = models.FloatField()
    marker = models.FloatField(null=True)
    objects = EarthDistanceQuerySet.as_manager()
    
    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'