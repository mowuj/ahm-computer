from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Category, Product,Brand
from .serializers import CategorySerializer, ProductSerializer,BrandSerializer
# Create your views here.


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class BrandViewset(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
