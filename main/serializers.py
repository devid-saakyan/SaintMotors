from rest_framework import serializers
from .models import *


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['image']


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, read_only=True)
    Logo = serializers.SerializerMethodField()
    FuelName = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = '__all__'

    def get_Logo(self, obj):
        request = self.context.get('request')
        logo_url = obj.Make.logo.url if obj.Make else None
        if logo_url and request:
            return request.build_absolute_uri(logo_url)
        return logo_url

    def get_FuelName(self, obj):
        return obj.Fuel.name if obj.Make else None


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