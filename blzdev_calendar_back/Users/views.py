import token
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from rest_framework.views import APIView
from .serializer import CreateSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny

class CreateAcoount(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            serializer = CreateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user=serializer.save()

            _, token = AuthToken.objects.create(user)

            return Response({
                'user_name': user.user_name,
                "token": token
            },
            status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class LoginAccount(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            serializer = AuthTokenSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            _, token = AuthToken.objects.create(user)
            return Response({
                'user_name': user.user_name,
                "token": token
            },
            status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)