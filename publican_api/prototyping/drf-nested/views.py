"""drf-nested_api profiling views"""

from drf_nested.models import Drink, Glass
from drf_nested.serializers import DrinkSerializer, GlassSerializer

from rest_framework import viewsets


class DrinkViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing drink instances.
    """
    serializer_class = DrinkSerializer
    queryset = Drink.objects.all()
# /DrinkViewSet


class GlassViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing glass instances.
    """
    serializer_class = GlassSerializer
    queryset = Glass.objects.all()
# /GlassViewSet


# EOF