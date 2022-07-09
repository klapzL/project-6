
from rest_framework import serializers
from .models import Product, ProductCategory, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'model', 'description', 'price', 'tags'
        )


class ProductWritableSeializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('tags',)
            # fields = (
            #     'model', 'description', 'price', 'category', 'manufacturer',
            # )


class ProdcutCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = '__all__'