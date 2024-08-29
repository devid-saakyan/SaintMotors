from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')
router.register(r'plates', PlatesViewSet, basename='plates')
router.register(r'submissions', CarSubmissionViewSet, basename='Submissions')
router.register(r'fuel', FuelTypeViewSet, basename='Fuel')
router.register(r'transmission', TransmissionTypeViewSet, basename='Transmission')
router.register(r'CallBack', CallBackViewSet, basename='CallBack')
router.register(r'TyreCondition', TyreConditionViewSet, basename='Tyre')
router.register(r'BodyTypes', BodyTypeViewSet, basename='Body')
router.register(r'Make', MakeViewSet, basename='Make')

urlpatterns = [
    path('', include(router.urls)),
]
