from django.urls import path
from .views import ProductList, ProductDetails, ProductDestroy, ProductUpdate, ProductCreate


urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/delete', ProductDestroy.as_view(), name='product_destroy'),
    path('<int:pk>/update', ProductUpdate.as_view(), name='product_update'),
    path('<int:pk>/', ProductDetails.as_view(), name='product_details'),
]