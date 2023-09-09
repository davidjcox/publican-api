"""drf-nested_api profiling serializers"""

from drf_nested.models import Drink, Glass

from rest_framework import serializers


class DrinkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Drink
# /DrinkSerializer


class GlassSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Glass
# /GlassSerializer


# EOF