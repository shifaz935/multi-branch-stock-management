from django.urls import path
from .views import product_list, stock_list, add_stock, add_product
# ...existing code...

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('stocks/', stock_list, name='stock_list'),
    path('add-stock/', add_stock, name='add_stock'),
    path('add-product/', add_product, name='add_product'),
]
