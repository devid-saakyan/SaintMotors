from rest_framework import serializers
from .models import *


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['image']

class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = '__all__'


class PlatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plates
        fields = '__all__'


class CarSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSubmission
        fields = '__all__'


class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = '__all__'


class TransmissionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransmissionType
        fields = '__all__'


class TyreConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TyreCondition
        fields = '__all__'


class BodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = '__all__'


class CallBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallBack
        fields = '__all__'