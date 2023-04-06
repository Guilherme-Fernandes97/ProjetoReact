from rest_framework import viewsets, status
from .models import Order, Company, Category, RealStateAgency, Users
from .serializers import OrderSerializer, CompanySerializer, CategorySerializer, RealStateSerializer
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer

    def get_queryset(self):
        return Company.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

class RealStateViewSet(viewsets.ModelViewSet):
    serializer_class = RealStateSerializer

    def get_queryset(self):
        return RealStateAgency.objects.all()

@permission_classes([AllowAny])
class SignupView(APIView):
    def post(self, request, format=None):
        # create user
        user = User.objects.create_user(
            username=request.data['username'], 
            password=request.data['password']
        )

        # create user profile
        user_profile = Users.objects.create(
            user=user,
            email=request.data['email']
        )

        # create token
        token, created = Token.objects.get_or_create(user=user)

        # return response
        return Response({
        }, status=status.HTTP_201_CREATED)



@api_view(['POST'])
@permission_classes([AllowAny])
def obtain_auth_token(request):
    """
    View para gerar um token de autenticação para um usuário.
    """
    username = request.data.get('username')
    password = request.data.get('password')
    
    if username is None or password is None:
        return Response({'error': 'Por favor, forneça o nome de usuário e a senha.'}, status=400)
    
    user = authenticate(username=username, password=password)
    
    if not user:
        return Response({'error': 'Não foi possível autenticar com as credenciais fornecidas.'}, status=400)
    
    token, _ = Token.objects.get_or_create(user=user)
    
    return Response({'token': token.key})
