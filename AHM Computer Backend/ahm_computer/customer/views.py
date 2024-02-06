from django.shortcuts import render, redirect
from . import serializers
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Customer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response("Welcome You successfully registered")
        return Response(serializer.errors)


class UserLoginView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                if user.is_staff:
                    # If user is an admin
                    login(request, user)
                    return Response({'message': "Welcome Admin!", 'user_id': user.id})
                else:
                    # If user is not an admin
                    login(request, user)
                    return Response({'message': "Welcome! You are successfully logged in.", 'user_id': user.id})
            else:
                return Response({'error': "Invalid Credentials"})
        return Response(serializer.errors)


class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')
