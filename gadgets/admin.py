from atexit import register
from django.contrib import admin
from .models import Manufacturer, ProductCategory, Product, House

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(House)