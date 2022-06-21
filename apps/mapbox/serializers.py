from rest_framework import serializers

from apps.mapbox.models import Shape


class ShapeSerializer(serializers.ModelSerializer):
    shape_region = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Shape
        fields = '__all__'

    def get_shape_region(self, instance):
        coords = instance.Shape_Area.coords
        return {
            "type": "box",
            "coordinates": {
                "x": coords[0][0][0],
                "y": coords[0][0][1],
                "h": coords[0][2][1] - coords[0][0][1],
                "w": coords[0][2][0] - coords[0][0][0],
            },
        }
