from rest_framework import viewsets
from .models import Car, Plates
from .serializers import CarSerializer, PlatesSerializer
from .pagination import CarPagination
from drf_spectacular.utils import extend_schema, OpenApiResponse

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