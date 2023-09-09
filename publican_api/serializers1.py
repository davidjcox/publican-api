"""publican_api serializers"""

from django.forms import widgets
from django.contrib.auth.models import User

from rest_framework import serializers

import publican_api.models as api_models


class BeerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.Beer
        
        fields = ('name', 
                  'ibu', 
                  'calories', 
                  'abv',)
        
        read_only_fields = ('slug', 
                            'overall_rating', 
                            'created', 
                            'updated',)
# /BeerSerializer


class WineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.Wine
        
        fields = ('name', 
                  'sweetness', 
                  'acidity', 
                  'tannin', 
                  'fruit',)
        
        read_only_fields = ('slug', 
                            'overall_rating', 
                            'created', 
                            'updated',)
# /WineSerializer


class LiquorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.Liquor
        
        fields = ('name', 
                  'abv', 
                  'calories',)
        
        read_only_fields = ('slug', 
                            'overall_rating', 
                            'created', 
                            'updated',)
# /LiquorSerializer


class BrewerySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.Brewery
        
        fields = ('name', 
                  'location', 
                  'beer',)
        
        read_only_fields = ('slug', 
                            'created', 
                            'updated',)
# /BrewerySerializer


class WinerySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.Winery
        
        fields = ('name', 
                  'location', 
                  'wine',)
        
        read_only_fields = ('slug', 
                            'created', 
                            'updated',)
# /WinerySerializer


class DistillerySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.Distillery
        
        fields = ('name', 
                  'location', 
                  'liquor',)
        
        read_only_fields = ('slug', 
                            'created', 
                            'updated',)
# /DistillerySerializer


class BeerGlassSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.BeerGlass
        
        fields = ('type', 
                  'beer',)
        
        read_only_fields = ('slug', 
                            'created', 
                            'updated',)
# /BeerGlassSerializer


class WineGlassSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.WineGlass
        
        fields = ('type', 
                  'wine',)
        
        read_only_fields = ('slug', 
                            'created', 
                            'updated',)
# /WineGlassSerializer


class LiquorGlassSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.LiquorGlass
        
        fields = ('type',  
                  'liquor',)
        
        read_only_fields = ('slug', 
                            'created', 
                            'updated',)
# /LiquorGlassSerializer


class BeerStyleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.BeerStyle
        
        fields = ('name', 
                  'beer',)
        
        read_only_fields = ('slug', 
                            'created', 
                            'updated',)
# /BeerStyleSerializer


class WineStyleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.WineStyle
        
        fields = ('name', 
                  'wine',)
        
        read_only_fields = ('slug', 
                            'created', 
                            'updated',)
# /WineStyleSerializer


class LiquorStyleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.LiquorStyle
        
        fields = ('name', 
                  'liquor',)
        
        read_only_fields = ('slug', 
                            'created', 
                            'updated',)
# /LiquorStyleSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)
# /UserSerializer


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
        MAX_RATING = 5
        msg = "Aroma should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_appearance(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 5
        msg = "Appearance should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_taste(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 10
        msg = "Taste should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_palate(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 5
        msg = "Palate should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_bottlestyle(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 5
        msg = "Bottle style should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
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
        MAX_RATING = 5
        msg = "Color should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_color(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 5
        msg = "Color should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_intensity(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 5
        msg = "Intensity should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_aroma(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 10
        msg = "Aroma should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_body(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 5
        msg = "Body should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_astringency(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 5
        msg = "Astringency should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_alcohol(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 5
        msg = "Alcohol should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_balance(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 10
        msg = "Balance should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_body(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 5
        msg = "Body should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_body(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 5
        msg = "Body should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_bottlestyle(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 5
        msg = "Bottle style should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
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
    
    def validate_appearance(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 5
        msg = "Appearance should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_aroma(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 5
        msg = "Aroma should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_taste(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 10
        msg = "Taste should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_aftertaste(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 5
        msg = "Aftertaste should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
    
    def validate_bottlestyle(self, attrs, source):
        value = attrs[source]
        MAX_RATING = 5
        msg = "Bottle style should be rated on a scale of 1 to " + MAX_RATING + "."
        if (value < 1) or (value > MAX_RATING):
            raise serializers.ValidationError(msg)
        return attrs
# /LiquorReviewSerializer


class InstallationDocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.InstallationDocument
        
        fields = ('name',)
        
        read_only_fields = ('slug', 
                            'version', 
                            'created', 
                            'updated',)
        
        contents = serializers.Field(source='read_source_file')
# /InstallationDocumentSerializer


class ExecutionDocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.ExecutionDocument
        
        fields = ('name',)
        
        read_only_fields = ('slug', 
                            'version', 
                            'created', 
                            'updated',)
        
        contents = serializers.Field(source='read_source_file')
# /ExecutionDocumentSerializer


class RequirementsDocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.RequirementsDocument
        
        fields = ('name',)
        
        read_only_fields = ('slug', 
                            'version', 
                            'created', 
                            'updated',)
        
        contents = serializers.Field(source='read_source_file')
# /RequirementsDocumentSerializer


class DefinitionsDocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.DefinitionsDocument
        
        fields = ('name',)
        
        read_only_fields = ('slug', 
                            'version', 
                            'created', 
                            'updated',)
        
        contents = serializers.Field(source='read_source_file')
# /DefinitionsDocumentSerializer


class BaseModelsDocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.BaseModelsDocument
        
        fields = ('name',)
        
        read_only_fields = ('slug', 
                            'version', 
                            'created', 
                            'updated',)
        
        contents = serializers.Field(source='read_source_file')
# /BaseModelsDocumentSerializer


class ModelsDocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.ModelsDocument
        
        fields = ('name',)
        
        read_only_fields = ('slug', 
                            'version', 
                            'created', 
                            'updated',)
        
        contents = serializers.Field(source='read_source_file')
# /ModelsDocumentSerializer


class ViewsDocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.ViewsDocument
        
        fields = ('name',)
        
        read_only_fields = ('slug', 
                            'version', 
                            'created', 
                            'updated',)
        
        contents = serializers.Field(source='read_source_file')
# /ViewsDocumentSerializer


class SerializersDocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.SerializersDocument
        
        fields = ('name',)
        
        read_only_fields = ('slug', 
                            'version', 
                            'created', 
                            'updated',)
        
        contents = serializers.Field(source='read_source_file')
# /SerializersDocumentSerializer


class ThrottlesDocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.ThrottlesDocument
        
        fields = ('name',)
        
        read_only_fields = ('slug', 
                            'version', 
                            'created', 
                            'updated',)
        
        contents = serializers.Field(source='read_source_file')
# /ThrottlesDocumentSerializer


class PermissionsDocumentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = api_models.PermissionsDocument
        
        fields = ('name',)
        
        read_only_fields = ('slug', 
                            'version', 
                            'created', 
                            'updated',)
        
        contents = serializers.Field(source='read_source_file')
# /PermissionsDocumentSerializer


# EOF - publican_api serializers