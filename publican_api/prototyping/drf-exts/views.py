"""drf_exts profiling views"""

from drf_exts.models import Drink, Glass
from drf_exts.serializers import DrinkSerializer, GlassSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin


class DrinkViewSet(NestedViewSetMixin, ModelViewSet):
    """
    A viewset for viewing and editing drink instances.
    """
    serializer_class = DrinkSerializer
    queryset = Drink.objects.all()
# /DrinkViewSet


class GlassViewSet(NestedViewSetMixin, ModelViewSet):
    """
    A viewset for viewing and editing glass instances.
    """
    serializer_class = GlassSerializer
    queryset = Glass.objects.all()
# /GlassViewSet


# EOF