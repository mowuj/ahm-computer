from .models import Customer
from rest_framework import serializers
from . models import Customer
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Customer
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    phone = serializers.CharField(write_only=True)
    gender = serializers.CharField(write_only=True)
    street_address = serializers.CharField(write_only=True)
    city = serializers.CharField(write_only=True)
    country = serializers.CharField(write_only=True)
    image = serializers.ImageField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password', 'confirm_password', 'phone', 'gender', 'street_address', 'city', 'country', 'image']

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError(
                {'error': 'Password Does not match'})

        email = data.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'error': 'Email already exists'})

        return data

    def create(self, validated_data):
        phone = validated_data.pop('phone')
        gender = validated_data.pop('gender')
        street_address = validated_data.pop('street_address')
        city = validated_data.pop('city')
        country = validated_data.pop('country')
        image = validated_data.pop('image')

        validated_data.pop('confirm_password', None)

        user = User.objects.create_user(**validated_data)

        Customer.objects.create(
            user=user,
            customer_id=10000 + user.id,
            phone=phone,
            gender=gender,
            street_address=street_address,
            city=city,
            country=country,
            image=image
        )

        return user

    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
