from rest_framework import viewsets
from .models import Order, Company, Category, RealStateAgency
from .serializers import OrderSerializer, CompanySerializer, CategorySerializer, RealStateSerializer


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