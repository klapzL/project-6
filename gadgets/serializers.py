from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        #fields = '__all__'
        fields = (
            'id', 'model', 'description', 'price'
        )


class ProductWritableSeializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'model', 'description', 'price', 'category', 'manufacturer',
        )