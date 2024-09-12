from rest_framework import serializers
from .models import *
from django.conf import settings

base_url = 'https://api.saintmotors.com'


class CarImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = CarImage
        fields = ['image']

    def get_image(self, obj):
        request = self.context.get('request')
        if not request:
            return request.build_absolute_uri(obj.image.url)
        return f"{base_url}{obj.image.url}"


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
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
        full_logo_url = f"{base_url}{logo_url}"
        return full_logo_url

    def get_FuelName(self, obj):
        return obj.Fuel.name if obj.Make else None


class PlatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plates
        fields = '__all__'


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhoto
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


class TyreBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = TyreBrand
        fields = '__all__'


class BodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = '__all__'


class CallBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallBack
        fields = '__all__'


class CarOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOption
        fields = ['id', 'name', 'category']


class OptionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionCategory
        fields = '__all__'


class OptionCategoryWithOptionsSerializer(serializers.ModelSerializer):
    option = CarOptionSerializer(many=True, read_only=True, source='options')

    class Meta:
        model = OptionCategory
        fields = ['id', 'name', 'option']


class HomepageSerializer(serializers.ModelSerializer):
    image1 = serializers.SerializerMethodField()
    image2 = serializers.SerializerMethodField()

    class Meta:
        model = Homepage
        fields = '__all__'

    def get_image1(self, obj):
        return f"{base_url}{obj.image1.url}"

    def get_image2(self, obj):
        return f"{base_url}{obj.image2.url}"
