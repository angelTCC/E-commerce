from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import View

# Create your views here.
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserRegistrationSerializerDRF

class UserRegistrationViewDRF(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializerDRF(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# views.py
def register_view(request):
    return render(request, 'register.html')


def close_session(request):
    logout(request)
    return render(request, 'home.html')
