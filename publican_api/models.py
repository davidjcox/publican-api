"""publican_api models"""

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify
from django.contrib import admin

import publican_api.basemodels as api_basemodels


class Favorite(models.Model):
    
    class Meta:
        app_label = settings.APP_LABEL
        get_latest_by = "created"
        
    favoriter = models.ForeignKey(User)
    
    url = models.URLField(max_length=100)
    
    resource_content_type = models.ForeignKey(ContentType)
    
    resource_object_id = models.PositiveIntegerField()
    
    favorited = generic.GenericForeignKey('resource_content_type', 
                                            'resource_object_id')
# /Favorite


class Beer(api_basemodels.Resource, api_basemodels.Drink):
    
    class Meta(api_basemodels.Resource.Meta):
        verbose_name_plural = "beers"
    
    favorites = generic.GenericRelation('Favorite', 
                                        related_query_name='beers', 
                                        content_type_field='resource_content_type', 
                                        object_id_field='resource_object_id')
    
    # range: 5-100
    ibu = models.PositiveSmallIntegerField("International Bitterness Units", 
                                           help_text="Range from 5-100.")
    
    # range: 50-1000
    calories = models.PositiveSmallIntegerField("Calories", 
                                                help_text="Range from 50-1000.")
    
    # range: 0-80
    abv = models.FloatField("Alcohol By Volume", 
                            help_text="Range from 0-80.")
# /Beer
admin.site.register(Beer)


class Wine(api_basemodels.Resource, api_basemodels.Drink):
    
    class Meta(api_basemodels.Resource.Meta):
        verbose_name_plural = "wines"
    
    TANNIN_CHOICES = (
        ('L', 'Low'), 
        ('H', 'High'),
    )
    
    favorites = generic.GenericRelation('Favorite', 
                                        related_query_name='wines', 
                                        content_type_field='resource_content_type', 
                                        object_id_field='resource_object_id')
    
    # range: 1-1000
    sweetness = models.PositiveSmallIntegerField("Sweetness", 
                                                 help_text="Range from 1-1000.")
    
    # range: 0.1-1.0
    acidity = models.FloatField("Acidity", 
                                help_text="Range from 0.1-1.0.")
    
    # range: low-high 
    tannin = models.CharField("Tannin", 
                              max_length=1,
                              choices=TANNIN_CHOICES, 
                              default='L')
    
    fruit = models.CharField("Fruit", 
                             max_length=128, 
                             blank=True, 
                             help_text="Optional, max 128 characters.")
# /Wine
admin.site.register(Wine)


class Liquor(api_basemodels.Resource, api_basemodels.Drink):
    
    class Meta(api_basemodels.Resource.Meta):
        verbose_name_plural = "liquors"
    
    favorites = generic.GenericRelation('Favorite', 
                                        related_query_name='liquors', 
                                        content_type_field='resource_content_type', 
                                        object_id_field='resource_object_id')
    
    # range: 50-1000
    calories = models.PositiveSmallIntegerField("Calories", 
                                                help_text="Range from 50-1000.")
    
    # range: 0-80
    abv = models.FloatField("Alcohol By Volume", 
                            help_text="Range from 0-80.")
# /Liquor
admin.site.register(Liquor)


class Brewery(api_basemodels.Resource, api_basemodels.Facility):
    
    class Meta(api_basemodels.Resource.Meta):
        verbose_name_plural = "breweries"
    
    beer = models.ForeignKey(Beer)
    
    favorites = generic.GenericRelation('Favorite', 
                                        related_query_name='breweries', 
                                        content_type_field='resource_content_type', 
                                        object_id_field='resource_object_id')
# /Brewery
admin.site.register(Brewery)


class Winery(api_basemodels.Resource, api_basemodels.Facility):
    
    class Meta(api_basemodels.Resource.Meta):
        verbose_name_plural = "wineries"
    
    wine = models.ForeignKey(Wine)
    
    favorites = generic.GenericRelation('Favorite', 
                                        related_query_name='wineries', 
                                        content_type_field='resource_content_type', 
                                        object_id_field='resource_object_id')
    
# /Winery
admin.site.register(Winery)


class Distillery(api_basemodels.Resource, api_basemodels.Facility):
    
    class Meta(api_basemodels.Resource.Meta):
        verbose_name_plural = "distilleries"
    
    liquor = models.ForeignKey(Liquor)
    
    favorites = generic.GenericRelation('Favorite', 
                                        related_query_name='distilleries', 
                                        content_type_field='resource_content_type', 
                                        object_id_field='resource_object_id')
# /Distillery
admin.site.register(Distillery)


class BeerGlass(api_basemodels.Resource, api_basemodels.Glass):
    
    class Meta(api_basemodels.Resource.Meta):
        verbose_name = "beer glass"
        verbose_name_plural = "beer glasses"
    
    beer = models.ForeignKey(Beer)
    
    favorites = generic.GenericRelation('Favorite', 
                                        related_query_name='beerglasses', 
                                        content_type_field='resource_content_type', 
                                        object_id_field='resource_object_id')
# /BeerGlass
admin.site.register(BeerGlass)


class WineGlass(api_basemodels.Resource, api_basemodels.Glass):
    
    class Meta(api_basemodels.Resource.Meta):
        verbose_name = "wine glass"
        verbose_name_plural = "wine glasses"
    
    wine = models.ForeignKey(Wine)
    
    favorites = generic.GenericRelation('Favorite', 
                                        related_query_name='wineglasses', 
                                        content_type_field='resource_content_type', 
                                        object_id_field='resource_object_id')
# /WineGlass
admin.site.register(WineGlass)


class LiquorGlass(api_basemodels.Resource, api_basemodels.Glass):
    
    class Meta(api_basemodels.Resource.Meta):
        verbose_name = "liquor glass"
        verbose_name_plural = "liquor glasses"
    
    liquor = models.ForeignKey(Liquor)
    
    favorites = generic.GenericRelation('Favorite', 
                                        related_query_name='liquorglasses', 
                                        content_type_field='resource_content_type', 
                                        object_id_field='resource_object_id')
# /LiquorGlass
admin.site.register(LiquorGlass)


class BeerStyle(api_basemodels.Resource, api_basemodels.Style):
    
    class Meta(api_basemodels.Resource.Meta):
        verbose_name = "beer style"
        verbose_name_plural = "beer styles"
    
    beer = models.ForeignKey(Beer)
    
    favorites = generic.GenericRelation('Favorite', 
                                        related_query_name='beerstyles', 
                                        content_type_field='resource_content_type', 
                                        object_id_field='resource_object_id')
# /BeerStyle
admin.site.register(BeerStyle)


class WineStyle(api_basemodels.Resource, api_basemodels.Style):
    
    class Meta(api_basemodels.Resource.Meta):
        verbose_name = "wine style"
        verbose_name_plural = "wine styles"
    
    wine = models.ForeignKey(Wine)
    
    favorites = generic.GenericRelation('Favorite', 
                                        related_query_name='winestyles', 
                                        content_type_field='resource_content_type', 
                                        object_id_field='resource_object_id')
# /WineStyle
admin.site.register(WineStyle)


class LiquorStyle(api_basemodels.Resource, api_basemodels.Style):
    
    class Meta(api_basemodels.Resource.Meta):
        verbose_name = "liquor style"
        verbose_name_plural = "liquor styles"
    
    liquor = models.ForeignKey(Liquor)
    
    favorites = generic.GenericRelation('Favorite', 
                                        related_query_name='liquorstyles', 
                                        content_type_field='resource_content_type', 
                                        object_id_field='resource_object_id')
# /LiquorStyle
admin.site.register(LiquorStyle)


class BeerReview(api_basemodels.Review):
    
    class Meta(api_basemodels.Review.Meta):
        verbose_name = "beer review"
        verbose_name_plural = "beer reviews"
    
    beer = models.ForeignKey(Beer)
    
    # range: 1-5
    appearance = models.PositiveSmallIntegerField("Appearance", 
                                                  default=0)
    
    # range: 1-5
    aroma = models.PositiveSmallIntegerField("Aroma", 
                                             default=0)
    
    # range: 1-10
    taste = models.PositiveSmallIntegerField("Taste", 
                                             default=0)
    
    # range: 1-5
    palate = models.PositiveSmallIntegerField("Palate", 
                                              default=0)
    
    # range: 1-5
    bottlestyle = models.PositiveSmallIntegerField("Bottle Style", 
                                                   default=0)
    
    def calculate_overall_rating(self):
        """
        1) Sum the total_ratings of all instances of reviews for this beer.
            aggregate_rating = sum([beer.total_rating for beer_review in beer_reviews])
        2) Divide summed ratings by beers.count() to get averaged rating.
            average_rating = aggregate_rating / beers.count()
        3) Ratchet average rating to final quarter fractional value.
            overall_beer_rating = round(DENOMINATOR * average_rating) / DENOMINATOR
        4) Return overall rating for this particular beer.
        """
        DENOMINATION = 4
        
        beer_reviews = BeerReview.objects.filter(beer=self.beer)
        aggregate_rating = sum([beer_review.total_rating 
                                for beer_review in beer_reviews])
        average_rating = aggregate_rating / beer_reviews.count()
        overall_beer_rating = round(DENOMINATION * average_rating) / DENOMINATION
        return overall_beer_rating
    
    def save(self, *args, **kwargs):
        """
        Pass a list of tuples of attributes and their respective rating weights.
        The weighted ratings are whole number percentages, so the sum of 
        weighted ratings must add up to 100.
        """
        self.slug = slugify(self.title)
        self.total_rating = self.calculate_total_rating([(self.appearance, 10,), 
                                                         (self.aroma, 25,), 
                                                         (self.taste, 45,), 
                                                         (self.palate, 15,), 
                                                         (self.bottlestyle, 5,)
                                                        ])
        super(BeerReview, self).save(*args, **kwargs)
        self.beer.overall_rating = self.calculate_overall_rating()
        self.beer.save()
# /BeerReview
admin.site.register(BeerReview)


class WineReview(api_basemodels.Review):
    
    class Meta(api_basemodels.Review.Meta):
        verbose_name = "wine review"
        verbose_name_plural = "wine reviews"
    
    wine = models.ForeignKey(Wine)
    
    # range: 1-5
    clarity = models.PositiveSmallIntegerField("Clarity", 
                                               default=0)
    
    # range: 1-5
    color = models.PositiveSmallIntegerField("Color", 
                                             default=0)
    
    # range: 1-5
    intensity = models.PositiveSmallIntegerField("Intensity", 
                                                 default=0)
    
    # range: 1-10
    aroma = models.PositiveSmallIntegerField("Aroma", 
                                             default=0)
    
    # range: 1-5
    body = models.PositiveSmallIntegerField("Body", 
                                            default=0)
    
    # range: 1-5
    astringency = models.PositiveSmallIntegerField("Astringency", 
                                                   default=0)
    
    # range: 1-5
    alcohol = models.PositiveSmallIntegerField("Alcohol", 
                                               default=0)
    
    # range: 1-10
    balance = models.PositiveSmallIntegerField("Balance", 
                                               default=0)
    
    # range: 1-10
    finish = models.PositiveSmallIntegerField("Finish", 
                                              default=0)
    
    # range: 1-10
    complexity = models.PositiveSmallIntegerField("Complexity", 
                                                  default=0)
    
    # range: 1-5
    bottlestyle = models.PositiveSmallIntegerField("Bottle Style", 
                                                   default=0)
    
    def calculate_overall_rating(self):
        """
        1) Sum the total_ratings of all instances of reviews for this wine.
            aggregate_rating = sum([wine.total_rating for wine_review in wine_reviews])
        2) Divide summed ratings by wine.count() to get averaged rating.
            average_rating = aggregate_rating / wines.count()
        3) Ratchet average rating to final quarter fractional value.
            overall_wine_rating = round(DENOMINATOR * average_rating) / DENOMINATOR
        4) Return overall rating for this particular wine.
        """
        DENOMINATION = 4
        
        wine_reviews = WineReview.objects.filter(wine=self.wine)
        aggregate_rating = sum([wine_review.total_rating 
                                for wine_review in wine_reviews])
        average_rating = aggregate_rating / wine_reviews.count()
        overall_wine_rating = round(DENOMINATION * average_rating) / DENOMINATION
        return overall_wine_rating
    
    def save(self, *args, **kwargs):
        """
        Pass a list of tuples of attributes and their respective rating weights.
        The weighted ratings are whole number percentages, so the sum of 
        weighted ratings must add up to 100.
        """
        self.slug = slugify(self.title)
        self.total_rating = self.calculate_total_rating([(self.clarity, 5), 
                                                         (self.color, 5), 
                                                         (self.intensity, 5), 
                                                         (self.aroma, 20), 
                                                         (self.body, 5), 
                                                         (self.astringency, 5), 
                                                         (self.alcohol, 5), 
                                                         (self.balance, 15), 
                                                         (self.finish, 15), 
                                                         (self.complexity, 15), 
                                                         (self.bottlestyle, 5)
                                                        ])
        super(WineReview, self).save(*args, **kwargs)
        self.wine.overall_rating = self.calculate_overall_rating()
        self.wine.save()
    # /WineReview
admin.site.register(WineReview)


class LiquorReview(api_basemodels.Review):
    
    class Meta(api_basemodels.Review.Meta):
        verbose_name = "liquor review"
        verbose_name_plural = "liquor reviews"
    
    liquor = models.ForeignKey(Liquor)
    
    # range: 1-5
    appearance = models.PositiveSmallIntegerField("Appearance", 
                                                  default=0)
    
    # range: 1-5
    aroma = models.PositiveSmallIntegerField("Aroma", 
                                             default=0)
    
    # range: 1-10
    taste = models.PositiveSmallIntegerField("Taste", 
                                             default=0)
    
    # range: 1-5
    aftertaste = models.PositiveSmallIntegerField("Aftertaste", 
                                                  default=0)
    
    def calculate_overall_rating(self):
        """
        1) Sum the total_ratings of all instances of reviews for this liquor.
            aggregate_rating = sum([liquor.total_rating for liquor_review in liquor_reviews])
        2) Divide summed ratings by liquor.count() to get averaged rating.
            average_rating = aggregate_rating / liquors.count()
        3) Ratchet average rating to final quarter fractional value.
            overall_liquor_rating = round(DENOMINATOR * average_rating) / DENOMINATOR
        4) Return overall rating for this particular liquor.
        """
        DENOMINATION = 4
        
        liquor_reviews = LiquorReview.objects.filter(liquor=self.liquor)
        aggregate_rating = sum([liquor_review.total_rating 
                                for liquor_review in liquor_reviews])
        average_rating = aggregate_rating / liquor_reviews.count()
        overall_liquor_rating = round(DENOMINATION * average_rating) / DENOMINATION
        return overall_liquor_rating
    
    def save(self, *args, **kwargs):
        """
        Pass a list of tuples of attributes and their respective rating weights.
        The weighted ratings are whole number percentages, so the sum of 
        weighted ratings must add up to 100.
        """
        self.slug = slugify(self.title)
        self.total_rating = self.calculate_total_rating([(self.appearance, 10), 
                                                        (self.aroma, 30), 
                                                        (self.taste, 45), 
                                                        (self.aftertaste, 15)
                                                       ])
        super(LiquorReview, self).save(*args, **kwargs)
        self.liquor.overall_rating = self.calculate_overall_rating()
        self.liquor.save()
    # /LiquorReview
admin.site.register(LiquorReview)


# EOF - publican_api models
