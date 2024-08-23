from rest_framework import serializers
from .models import Car, CarImage, Plates


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