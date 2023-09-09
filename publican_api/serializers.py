"""publican_api serializers"""

from django.forms import widgets
from django.contrib.auth.models import User

from rest_framework import serializers

import publican_api.models as api_models


def get_msg(_attribute='', _min=0, _max=1):
    _fragment = " value should be between {0} to {1}."
    return _attribute + _fragment.format(_min, _max)


class BeerSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = api_models.Beer
        
        fields = ('name', 
                  'id', 
                  'url', 
                  'slug', 
                  'ibu', 
                  'calories', 
                  'abv', 
                  'overall_rating', 
                  'created', 
                  'updated',)
        
        read_only_fields = ('id', 
                            'slug', 
                            'overall_rating', 
                            'created', 
                            'updated',)
    
    def validate_ibu(self, attrs, source):
        value = attrs[source]
        MIN_VALUE = 5
        MAX_VALUE = 100
        msg = get_msg("IBU", MIN_VALUE, MAX_VALUE)
        if (value < MIN_VALUE) or (value > MAX_VALUE):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_calories(self, attrs, source):
        value = attrs[source]
        MIN_VALUE = 50
        MAX_VALUE = 1000
        msg = get_msg("Calories", MIN_VALUE, MAX_VALUE)
        if (value < MIN_VALUE) or (value > MAX_VALUE):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_abv(self, attrs, source):
        value = attrs[source]
        MIN_VALUE = 0
        MAX_VALUE = 80
        msg = get_msg("ABV", MIN_VALUE, MAX_VALUE)
        if (value < MIN_VALUE) or (value > MAX_VALUE):
            raise serializers.ValidationError(msg)
        return attrs
    
# /BeerSerializer


class WineSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = api_models.Wine
        
        fields = ('name', 
                  'id', 
                  'url', 
                  'slug', 
                  'sweetness', 
                  'acidity', 
                  'tannin', 
                  'fruit', 
                  'overall_rating', 
                  'created', 
                  'updated',)
        
        read_only_fields = ('id', 
                            'slug', 
                            'overall_rating', 
                            'created', 
                            'updated',)
    
    def validate_sweetness(self, attrs, source):
        value = attrs[source]
        MIN_VALUE = 1
        MAX_VALUE = 1000
        msg = get_msg("Sweetness", MIN_VALUE, MAX_VALUE)
        if (value < MIN_VALUE) or (value > MAX_VALUE):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_acidity(self, attrs, source):
        value = attrs[source]
        MIN_VALUE = 0.1
        MAX_VALUE = 1.0
        msg = get_msg("Acidity", MIN_VALUE, MAX_VALUE)
        if (value < MIN_VALUE) or (value > MAX_VALUE):
            raise serializers.ValidationError(msg)
        return attrs
    
# /WineSerializer


class LiquorSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = api_models.Liquor
        
        fields = ('name', 
                  'id', 
                  'url', 
                  'slug', 
                  'abv', 
                  'calories', 
                  'overall_rating', 
                  'created', 
                  'updated',)
        
        read_only_fields = ('id', 
                            'slug', 
                            'overall_rating', 
                            'created', 
                            'updated',)
    
    def validate_calories(self, attrs, source):
        value = attrs[source]
        MIN_VALUE = 50
        MAX_VALUE = 1000
        msg = get_msg("Calories", MIN_VALUE, MAX_VALUE)
        if (value < MIN_VALUE) or (value > MAX_VALUE):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_abv(self, attrs, source):
        value = attrs[source]
        MIN_VALUE = 0
        MAX_VALUE = 80
        msg = get_msg("ABV", MIN_VALUE, MAX_VALUE)
        if (value < MIN_VALUE) or (value > MAX_VALUE):
            raise serializers.ValidationError(msg)
        return attrs
    
# /LiquorSerializer


class BrewerySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = api_models.Brewery
        
        fields = ('name', 
                  'id', 
                  'url', 
                  'slug', 
                  'location', 
                  'beer', 
                  'created', 
                  'updated',)
        
        read_only_fields = ('id', 
                            'slug', 
                            'created', 
                            'updated',)
# /BrewerySerializer


class WinerySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = api_models.Winery
        
        fields = ('name', 
                  'id', 
                  'url', 
                  'slug', 
                  'location', 
                  'wine', 
                  'created', 
                  'updated',)
        
        read_only_fields = ('id', 
                            'slug', 
                            'created', 
                            'updated',)
# /WinerySerializer


class DistillerySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = api_models.Distillery
        
        fields = ('name', 
                  'id', 
                  'url', 
                  'slug', 
                  'location', 
                  'liquor', 
                  'updated',
                  'updated',)
        
        read_only_fields = ('id', 
                            'slug', 
                            'created', 
                            'updated',)
# /DistillerySerializer


class BeerGlassSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = api_models.BeerGlass
        
        fields = ('name', 
                  'id', 
                  'url', 
                  'slug', 
                  'type', 
                  'beer', 
                  'created', 
                  'updated',)
        
        read_only_fields = ('id', 
                            'slug', 
                            'created', 
                            'updated',)
# /BeerGlassSerializer


class WineGlassSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = api_models.WineGlass
        
        fields = ('name', 
                  'id', 
                  'url', 
                  'slug', 
                  'type', 
                  'wine', 
                  'created', 
                  'updated',)
        
        read_only_fields = ('id', 
                            'slug', 
                            'created', 
                            'updated',)
# /WineGlassSerializer


class LiquorGlassSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = api_models.LiquorGlass
        
        fields = ('name', 
                  'id', 
                  'url', 
                  'slug', 
                  'type', 
                  'liquor', 
                  'created', 
                  'updated',)
        
        read_only_fields = ('id', 
                            'slug', 
                            'created', 
                            'updated',)
# /LiquorGlassSerializer


class BeerStyleSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = api_models.BeerStyle
        
        fields = ('name', 
                  'id', 
                  'url', 
                  'slug', 
                  'description', 
                  'beer', 
                  'created', 
                  'updated',)
        
        read_only_fields = ('id', 
                            'slug', 
                            'created', 
                            'updated',)
# /BeerStyleSerializer


class WineStyleSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = api_models.WineStyle
        
        fields = ('name', 
                  'id', 
                  'url', 
                  'slug', 
                  'description', 
                  'wine', 
                  'created', 
                  'updated',)
        
        read_only_fields = ('id', 
                            'slug', 
                            'created', 
                            'updated',)
# /WineStyleSerializer


class LiquorStyleSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = api_models.LiquorStyle
        
        fields = ('name', 
                  'id', 
                  'url', 
                  'slug', 
                  'description', 
                  'liquor', 
                  'created', 
                  'updated',)
        
        read_only_fields = ('id', 
                            'slug', 
                            'created', 
                            'updated',)
# /LiquorStyleSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username', 
                  'id', 
                  'url',)
        
        read_only_fields = ('id',)
        
        extra_kwargs = {
                        'users': {'lookup_field': 'username'}
                       }
# /UserSerializer


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = api_models.Favorite
        
        fields = ('favoriter', 
                  'favorited', 
                  'created', 
                  'updated',)
        
        read_only_fields = ('created', 
                            'updated',)
        
# /FavoriteSerializer


class BeerReviewSerializer(serializers.Serializer):
    
    beer = BeerSerializer()
    
    rater = UserSerializer()
    
    aroma = serializers.IntegerField()
    # range: 1-5
    
    appearance = serializers.IntegerField()
    # range: 1-5
    
    taste = serializers.IntegerField()
    # range: 1-10
    
    palate = serializers.IntegerField()
    # range: 1-5
    
    bottlestyle = serializers.IntegerField()
    # range: 1-5
    
    description = serializers.CharField(required=False, 
                                        widget=widgets.Textarea)
    
    def validate_aroma(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 5
        msg = get_msg("Aroma", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_appearance(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 5
        msg = get_msg("Appearance", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_taste(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 10
        msg = get_msg("Taste", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_palate(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 5
        msg = get_msg("Palate", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_bottlestyle(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 5
        msg = get_msg("Bottle style", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
# /BeerReviewSerializer


class WineReviewSerializer(serializers.Serializer):
    
    wine = WineSerializer()
    
    rater = UserSerializer()
    
    clarity = serializers.IntegerField()
    # range: 1-5
    
    color = serializers.IntegerField()
    # range: 1-5
    
    intensity = serializers.IntegerField()
    # range: 1-5
    
    aroma = serializers.IntegerField()
    # range: 1-20
    
    body = serializers.IntegerField()
    # range: 1-5
    
    astringency = serializers.IntegerField()
    # range: 1-5
    
    alcohol = serializers.IntegerField()
    # range: 1-5
    
    balance = serializers.IntegerField()
    # range: 1-15
    
    finish = serializers.IntegerField()
    # range: 1-15
    
    complexity = serializers.IntegerField()
    # range: 1-15
    
    bottlestyle = serializers.IntegerField()
    # range: 1-5
    
    description = serializers.CharField(required=False, 
                                        widget=widgets.Textarea)
    
    def validate_clarity(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 5
        msg = get_msg("Clarity", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_color(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 5
        msg = get_msg("Color", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_intensity(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 5
        msg = get_msg("Intensity", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_aroma(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 20
        msg = get_msg("Aroma", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_body(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 5
        msg = get_msg("Body", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_astringency(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 5
        msg = get_msg("Astringency", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_alcohol(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 5
        msg = get_msg("Alcohol", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_balance(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 15
        msg = get_msg("Balance", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_finish(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 15
        msg = get_msg("Finish", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_complexity(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 15
        msg = get_msg("Complexity", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_bottlestyle(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 5
        msg = get_msg("Bottle style", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
# /WineReviewSerializer


class LiquorReviewSerializer(serializers.Serializer):
    
    liquor = LiquorSerializer()
    
    rater = UserSerializer()
    
    appearance = serializers.IntegerField()
    # range: 1-5
    
    aroma = serializers.IntegerField()
    # range: 1-5
    
    taste = serializers.IntegerField()
    # range: 1-10
    
    aftertaste = serializers.IntegerField()
    # range: 1-5
    
    bottlestyle = serializers.IntegerField()
    # range: 1-5
    
    description = serializers.CharField(required=False, 
                                        widget=widgets.Textarea)
    
    FRAGMENT = " should be rated on a scale of {0} to {1}."
    
    def validate_appearance(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 5
        msg = get_msg("Appearance", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_aroma(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 5
        msg = get_msg("Aroma", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_taste(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 10
        msg = get_msg("Taste", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_aftertaste(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 5
        msg = get_msg("Aftertaste", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_bottlestyle(self, attrs, source):
        value = attrs[source]
        MIN_RATING = 1
        MAX_RATING = 5
        msg = get_msg("Bottle style", MIN_VALUE, MAX_VALUE)
        if (value < MIN_RATING) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
# /LiquorReviewSerializer


# EOF - publican_api serializers