from django.urls import path
from .views import ProductList, ProductDetails, ProductDestroy, ProductUpdate, ProductCreate, CategoryListCreate, CategoryRetrieveUpdateDestroy


urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/product-categories/', CategoryRetrieveUpdateDestroy.as_view()),
    path('<int:pk>/delete/', ProductDestroy.as_view(), name='product_destroy'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('<int:pk>/', ProductDetails.as_view(), name='product_details'),
    path('product-categories/', CategoryListCreate.as_view()),
]