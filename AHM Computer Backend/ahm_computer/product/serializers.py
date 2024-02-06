
from rest_framework import serializers
from . models import Product,Category,Brand
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True)
    brand = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(), many=True)


    class Meta:
        model = Product
        fields = '__all__'
