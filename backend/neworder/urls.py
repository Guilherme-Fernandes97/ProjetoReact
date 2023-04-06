from .views import OrderViewSet, CompanyViewSet, CategoryViewSet, RealStateViewSet, obtain_auth_token, SignupView
from rest_framework import routers
from django.urls import re_path, include, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


router = routers.SimpleRouter()

router.register('order', OrderViewSet, basename='order', )
router.register('company', CompanyViewSet, basename='company', )
router.register('category', CategoryViewSet, basename='category', )
router.register('realstate', RealStateViewSet, basename='realstate', )


urlpatterns = [
    re_path(r'^', include(router.urls)),
    path('login/', obtain_auth_token, name='token_obtain_pair'),
    path('signup/', SignupView.as_view(), name='signup'),

]
