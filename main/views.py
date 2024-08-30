from rest_framework import viewsets
from .models import Car, Plates
from .serializers import *
from .pagination import CarPagination
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render, redirect
from .forms import CarSubmissionForm

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
        return super().list(request, *args, **kwargs)



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


class BodyTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Body.objects.all()
    serializer_class = BodyTypeSerializer


class MakeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Make.objects.all()
    serializer_class = MakeSerializer


@api_view(['POST'])
def car_submission_api(request):
    if request.method == 'POST':
        serializer = CarSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def call_back_api(request):
    if request.method == 'POST':
        serializer = CallBackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)