from django.urls import path, include
from .views import OrderViewSet, CompanyViewSet, CategoryViewSet, RealStateViewSet
from rest_framework import routers
from django.urls import re_path, include, path



router = routers.SimpleRouter()

router.register('order', OrderViewSet, basename='order', )
router.register('company', CompanyViewSet, basename='company', )
router.register('category', CategoryViewSet, basename='category', )
router.register('realstate', RealStateViewSet, basename='realstate', )


urlpatterns = [
    re_path(r'^', include(router.urls)),
]