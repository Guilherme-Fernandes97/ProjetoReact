from django.contrib import admin
from .models import Order, Category, RealStateAgency, Company

# Register your models here.
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(RealStateAgency)
admin.site.register(Company)
