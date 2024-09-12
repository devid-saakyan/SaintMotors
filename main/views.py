from rest_framework import viewsets
from .models import Car, Plates
from .serializers import *
from .pagination import CarPagination
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiTypes
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('id')
    serializer_class = CarSerializer
    pagination_class = CarPagination

    @extend_schema(
        responses={
            200: OpenApiResponse(
                description="Car list with pagination",
                response={
                    "type": "object",
                    "properties": {
                        "pageCount": {"type": "integer", "example": 10},
                        "itemCount": {"type": "integer", "example": 100},
                        "currentPage": {"type": "integer", "example": 1},
                        "pageSize": {"type": "integer", "example": 10},
                        "results": {
                            "type": "array",
                            "items": CarSerializer(),
                        },
                    },
                }
            )
        }
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='options')
    def get_options(self, request, pk=None):
        car = self.get_object()
        option = car.Options.all()
        categories = OptionCategory.objects.filter(options__in=option).distinct()
        serializer = OptionCategoryWithOptionsSerializer(categories, many=True)
        return Response(serializer.data)


class PlatesViewSet(viewsets.ModelViewSet):
    queryset = Plates.objects.all().order_by('id')
    serializer_class = PlatesSerializer
    pagination_class = CarPagination

    @extend_schema(
        responses={
            200: OpenApiResponse(
                description="Car list with pagination",
                response={
                    "type": "object",
                    "properties": {
                        "pageCount": {"type": "integer", "example": 10},
                        "itemCount": {"type": "integer", "example": 100},
                        "currentPage": {"type": "integer", "example": 1},
                        "pageSize": {"type": "integer", "example": 10},
                        "results": {
                            "type": "array",
                            "items": PlatesSerializer(),
                        },
                    },
                }
            )
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class CarSubmissionViewSet(viewsets.ModelViewSet):
    queryset = CarSubmission.objects.all()
    serializer_class = CarSubmissionSerializer


class CallBackViewSet(viewsets.ModelViewSet):
    queryset = CallBack.objects.all()
    serializer_class = CallBackSerializer


class FuelTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer


class TransmissionTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TransmissionType.objects.all()
    serializer_class = TransmissionTypeSerializer


class TyreConditionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TyreCondition.objects.all()
    serializer_class = TyreConditionSerializer


class TyreBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TyreBrand.objects.all()
    serializer_class = TyreBrandSerializer


class BodyTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Body.objects.all()
    serializer_class = BodyTypeSerializer


class MakeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Make.objects.all()
    serializer_class = MakeSerializer


class ModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

    @action(detail=True, methods=['get'])
    def by_make(self, request, pk=None):
        make = Make.objects.get(pk=pk)
        models = Model.objects.filter(make=make)
        serializer = self.get_serializer(models, many=True)
        return Response(serializer.data)


class CarOptionsSet(viewsets.ReadOnlyModelViewSet):
    queryset = CarOption.objects.all()
    serializer_class = CarOptionSerializer


class OptionCategorySet(viewsets.ReadOnlyModelViewSet):
    queryset = OptionCategory.objects.all()
    serializer_class = OptionCategoryWithOptionsSerializer


class ColorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class HomepageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Homepage.objects.all()
    serializer_class = HomepageSerializer


@api_view(['POST'])
def car_submission_api(request):
    if request.method == 'POST':
        serializer = CarSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            car_submission = serializer.save()
            return Response({'id': car_submission.id, **serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def call_back_api(request):
    if request.method == 'POST':
        serializer = CallBackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    request={
        'multipart/form-data': {
            'properties': {
                'images': {
                    'type': 'array',
                    'items': {
                        'type': 'string',
                        'format': 'binary'
                    }
                }
            }
        }
    },
    responses={201: CarPhotoSerializer(many=True)},
)
class CarPhotoUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, car_submission_id):
        try:
            car_submission = CarSubmission.objects.get(id=car_submission_id)
        except CarSubmission.DoesNotExist:
            return Response({"error": "CarSubmission not found"}, status=status.HTTP_404_NOT_FOUND)

        files = request.FILES.getlist('images')
        photos = []
        for file in files:
            photo = CarPhoto(car_submission=car_submission, image=file)
            photo.save()
            photos.append(photo)

        serializer = CarPhotoSerializer(photos, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)