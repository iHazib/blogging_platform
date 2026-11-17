from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
from rest_framework import generics
from .serializers import UserRegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomLoginSerializer

# @api_view(['POST'])
# def register_user(request):
#     serializer = UserRegistrationSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = []  # permission is open, no need of token. 

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomLoginSerializer # serialized class json response on login success.
