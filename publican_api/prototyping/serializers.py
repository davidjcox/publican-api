"""beermeister serializers"""

from rest_framework import serializers

class BeerBrewerySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BeerBrewery
        fields = ('name', 'location', 'created', 'updated')
# /BeerBrewerySerializer

class BeerGlassSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BeerGlass
        fields = ('type', 'created', 'updated')
# /BeerGlassSerializer

class BeerStyleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BeerStyle
        fields = ('style', 'created', 'updated')
# /BeerStyleSerializer

class BeerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Beer
        fields = ('name', 'ibu', 'calories', 'abv', 'brewery', 'glass', 'style', 'created', 'updated')
# /BeerSerializer

class BeerReviewSerializer(serializers.Serializer):
    
    class Meta:
        model = BeerReview
        fields = ('beer', 'rater', 'aroma', 'appearance', 'taste', 'palate', 'bottlestyle', 'description', 'created', 'updated')
    
    def validate_aroma(self, attrs, source):
        value = attrs[source]
        if (value < 1) or (value > 5):
            raise serializers.ValidationError("Aroma should be rated on a scale of 1 to 5.")
        return attrs
    
    def validate_appearance(self, attrs, source):
        value = attrs[source]
        if (value < 1) or (value > 5):
            raise serializers.ValidationError("Appearance should be rated on a scale of 1 to 5.")
        return attrs
    
    def validate_taste(self, attrs, source):
        value = attrs[source]
        if (value < 1) or (value > 10):
            raise serializers.ValidationError("Taste should be rated on a scale of 1 to 10.")
        return attrs
    
    def validate_palate(self, attrs, source):
        value = attrs[source]
        if (value < 1) or (value > 5):
            raise serializers.ValidationError("Palate should be rated on a scale of 1 to 5.")
        return attrs
    
    def validate_bottlestyle(self, attrs, source):
        value = attrs[source]
        if (value < 1) or (value > 5):
            raise serializers.ValidationError("Bottle style should be rated on a scale of 1 to 5.")
        return attrs
    
# /BeerReviewSerializer

class DocumentationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Documentation
        fields = ('latestversion', 'name', 'contents')
# /DocumentationSerializer

class SourceCodeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SourceCode
# /SourceCodeSerializer

# EOF - beermeister serializers.py