from rest_framework import viewsets
from django.shortcuts import render
from ..models import Product
from .serializers import ProductSerializer
class ProductListView(viewsets.ModelViewSet): 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer