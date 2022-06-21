from django.urls import path

from apps.mapbox import views

urlpatterns = [
    path("", views.ShapeViewSet.as_view({'get': 'list'}), name="test")
]
