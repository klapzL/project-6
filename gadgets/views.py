from django.shortcuts import render
from rest_framework import generics
from .models import Product, ProductCategory
from .serializers import ProductSerializer, ProductWritableSeializer, ProdcutCategorySerializer

# Create your views here.
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetails(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDestroy(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdate(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWritableSeializer


class ProductCreate(generics.CreateAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductWritableSeializer


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProdcutCategorySerializer


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProdcutCategorySerializer


def product_list_with_categories(request):
    products = Product.objects.prefetch_related('tags').all()
    context = {
        'products': products,
    }
    return render(request, 'gadgets/product_list_with_categories.html', context)
