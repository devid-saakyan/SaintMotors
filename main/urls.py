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
router.register(r'TyreBrand', TyreBrandViewSet, basename='TyreBrand')
router.register(r'BodyTypes', BodyTypeViewSet, basename='Body')
router.register(r'Make', MakeViewSet, basename='Make')
router.register(r'Model', ModelViewSet, basename='Model')
router.register(r'Color', ColorViewSet, basename='Color')


urlpatterns = [
    path('', include(router.urls)),
    path('car-submissions/<int:car_submission_id>/upload-photos/', CarPhotoUploadView.as_view(), name='upload-car-photos'),
]
