
from rest_framework import serializers
from . models import Cart, CartProduct, Order
from customer.models import Customer
from django.contrib.auth.models import User

class CartSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(many=False)

    class Meta:
        model = Cart
        fields = '__all__'


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
