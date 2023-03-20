from django.db import models
from rest_framework import serializers
from .models import Order, Company, Category, RealStateAgency

class OrderSerializer(serializers.ModelSerializer):

    company_name = serializers.CharField(source='company.name', required=False, read_only=True)
    category_name = serializers.CharField(source='category.name', required=False, read_only=True)
    real_state_name = serializers.CharField(source='real_state.name', required=False, read_only=True)

    class Meta:
        model = Order
        fields = (

            'id',
            'contact_name',
            'contact_phone',
            'real_state',
            'order_description',
            'company',
            'category',
            'deadline',
            'company_name',
            'category_name',
            'real_state_name',

        )

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
            'id',
            'name',
        )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


class RealStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = RealStateAgency
        fields = (
            'id',
            'name',
        )


