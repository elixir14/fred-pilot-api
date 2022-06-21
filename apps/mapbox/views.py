from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from apps.mapbox.models import Shape
from apps.mapbox.serializers import ShapeSerializer


@method_decorator(name='list', decorator=swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter('building_id', openapi.IN_QUERY, description="Building ID", type=openapi.TYPE_NUMBER),
        openapi.Parameter('latitude', openapi.IN_QUERY, description="Latitude", type=openapi.TYPE_NUMBER),
        openapi.Parameter('longitude', openapi.IN_QUERY, description="Longitude", type=openapi.TYPE_NUMBER)
    ]
))
class ShapeViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = ShapeSerializer
    queryset = Shape.objects.all()
    filterset_fields = ["byggid", "latitude", "longitude"]

    def get_queryset(self):
        query_params = self.request.query_params
        building_id = query_params.get('building_id')
        latitude = query_params.get('latitude')
        longitude = query_params.get('longitude')
        if latitude and longitude:
            queryset = Shape.objects.filter(latitude=latitude, longitude=longitude)
        elif building_id:
            queryset = Shape.objects.filter(byggid=building_id)
        else:
            queryset = Shape.objects.all()
        return queryset
