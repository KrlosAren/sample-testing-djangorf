from django.urls import include, path
from rest_framework.routers import  SimpleRouter

from .views import ProductViewSet

router = SimpleRouter()

router.register(r'products', viewset=ProductViewSet,basename='products')

urlpatterns = [
    path('', include(router.urls)),
]