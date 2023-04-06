from django.contrib import admin
from .models import Order, Category, RealStateAgency, Company, Users
from rest_framework.authtoken.models import TokenProxy 


admin.site.register(Order)
admin.site.register(Category)
admin.site.register(RealStateAgency)
admin.site.register(Company)
admin.site.register(Users)

