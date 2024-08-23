from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, PlatesViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')
router.register(r'plates', PlatesViewSet, basename='plates')

urlpatterns = [
    path('', include(router.urls)),
]
