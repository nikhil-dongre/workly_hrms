from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializers
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class UserRegister(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
            
        serializer = UserRegisterSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(TokenObtainPairView):
    pass