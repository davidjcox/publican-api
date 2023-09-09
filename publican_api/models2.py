"""publican_api models"""

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.contrib import admin

import publican_api.basemodels as api_basemodels
import publican_api.utils as api_utils


def get_class_name(verbose_name=None):
    return verbose_name.replace("-", "")


class Favorite(models.Model):
    
    class Meta:
        app_label = api_utils.get_app_label()
        get_latest_by = "created"
        
    user = models.ForeignKey(User)
    
    resource_content_type = models.ForeignKey(ContentType)
    
    resource_object_id = models.PositiveIntegerField()
    
    favorite_of = generic.GenericForeignKey('resource_content_type', 
                                            'resource_object_id')
    
    def __str__(self):
        return "{0}:{1}".format(self.user__name, self.favorite_of__name)
# /Favorite


class Beer(api_basemodels.Drink):
    
    class Meta(api_basemodels.Drink.Meta):
        verbose_name_plural = "beers"
    
    # range: 5-100
    ibu = models.PositiveSmallIntegerField("International Bitterness Units", 
                                           help_text="Range from 5-100.")
    
    # range: 50-1000
    calories = models.PositiveSmallIntegerField("Calories", 
                                                help_text="Range from 50-1000.")
    
    # range: 0-80
    abv = models.FloatField("Alcohol By Volume", 
                            help_text="Range from 0-80.")
    
    def get_absolute_url(self):
        return reverse('drink_retrieve_update_destroy', 
                       kwargs={'drink':get_class_name(self._meta.verbose_name_plural),
                       'drink_id':str(self.id)})
# /Beer
admin.site.register(Beer)


class Wine(api_basemodels.Drink):
    
    class Meta(api_basemodels.Drink.Meta):
        verbose_name_plural = "wines"
    
    TANNIN_CHOICES = (
        ('L', 'Low'), 
        ('H', 'High'),
    )
    
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
                             help_text="Max 128 characters.")
    
    def get_absolute_url(self):
        return reverse('drink_retrieve_update_destroy', 
                       kwargs={'drink':get_class_name(self._meta.verbose_name_plural), 
                       'drink_id':str(self.id)})
# /Wine
admin.site.register(Wine)


class Liquor(api_basemodels.Drink):
    
    class Meta(api_basemodels.Drink.Meta):
        verbose_name_plural = "liquors"
    
    # range: 50-1000
    calories = models.PositiveSmallIntegerField("Calories", 
                                                help_text="Range from 50-1000.")
    
    # range: 0-80
    abv = models.FloatField("Alcohol By Volume", 
                            help_text="Range from 0-80.")
    
    def get_absolute_url(self):
        return reverse('drink_retrieve_update_destroy', 
                       kwargs={'drink':get_class_name(self._meta.verbose_name_plural), 
                       'drink_id':str(self.id)})
# /Liquor
admin.site.register(Liquor)


class Brewery(api_basemodels.Facility):
    
    class Meta(api_basemodels.Facility.Meta):
        verbose_name_plural = "breweries"
    
    beer = models.ForeignKey(Beer)
    
    def get_absolute_url(self):
        return reverse('facility_retrieve_update_destroy', 
                       kwargs={'facility':get_class_name(self._meta.verbose_name_plural), 
                       'facility_id':str(self.id)})
# /Brewery
admin.site.register(Brewery)


class Winery(api_basemodels.Facility):
    
    class Meta(api_basemodels.Facility.Meta):
        verbose_name_plural = "wineries"
    
    wine = models.ForeignKey(Wine)
    
    def get_absolute_url(self):
        return reverse('facility_retrieve_update_destroy', 
                       kwargs={'facility':get_class_name(self._meta.verbose_name_plural), 
                       'facility_id':str(self.id)})
# /Winery
admin.site.register(Winery)


class Distillery(api_basemodels.Facility):
    
    class Meta(api_basemodels.Facility.Meta):
        verbose_name_plural = "distilleries"
    
    liquor = models.ForeignKey(Liquor)
    
    def get_absolute_url(self):
        return reverse('facility_retrieve_update_destroy', 
                       kwargs={'facility':get_class_name(self._meta.verbose_name_plural), 
                       'facility_id':str(self.id)})
# /Distillery
admin.site.register(Distillery)


class BeerGlass(api_basemodels.Glass):
    
    class Meta(api_basemodels.Glass.Meta):
        verbose_name = "beer-glass"
        verbose_name_plural = "beer-glasses"
    
    beer = models.ForeignKey(Beer)
    
    def get_absolute_url(self):
        return reverse('glass_retrieve_update_destroy', 
                       kwargs={'glass':get_class_name(self._meta.verbose_name_plural), 
                       'glass_id':str(self.id)})
# /BeerGlass
admin.site.register(BeerGlass)


class WineGlass(api_basemodels.Glass):
    
    class Meta(api_basemodels.Glass.Meta):
        verbose_name = "wine-glass"
        verbose_name_plural = "wine-glasses"
    
    wine = models.ForeignKey(Wine)
    
    def get_absolute_url(self):
        return reverse('glass_retrieve_update_destroy', 
                       kwargs={'glass':get_class_name(self._meta.verbose_name_plural), 
                       'glass_id':str(self.id)})
# /WineGlass
admin.site.register(WineGlass)


class LiquorGlass(api_basemodels.Glass):
    
    class Meta(api_basemodels.Glass.Meta):
        verbose_name = "liquor-glass"
        verbose_name_plural = "liquor-glasses"
    
    liquor = models.ForeignKey(Liquor)
    
    def get_absolute_url(self):
        return reverse('glass_retrieve_update_destroy', 
                       kwargs={'glass':get_class_name(self._meta.verbose_name_plural), 
                       'glass_id':str(self.id)})
# /LiquorGlass
admin.site.register(LiquorGlass)


class BeerStyle(api_basemodels.Style):
    
    class Meta(api_basemodels.Style.Meta):
        verbose_name = "beer-style"
        verbose_name_plural = "beer-styles"
    
    beer = models.ForeignKey(Beer)
    
    def get_absolute_url(self):
        return reverse('style_retrieve_update_destroy', 
                       kwargs={'style':get_class_name(self._meta.verbose_name_plural), 
                       'style_id':str(self.id)})
# /BeerStyle
admin.site.register(BeerStyle)


class WineStyle(api_basemodels.Style):
    
    class Meta(api_basemodels.Style.Meta):
        verbose_name = "wine-style"
        verbose_name_plural = "wine-styles"
    
    wine = models.ForeignKey(Wine)
    
    def get_absolute_url(self):
        return reverse('style_retrieve_update_destroy', 
                       kwargs={'style':get_class_name(self._meta.verbose_name_plural), 
                       'style_id':str(self.id)})
# /WineStyle
admin.site.register(WineStyle)


class LiquorStyle(api_basemodels.Style):
    
    class Meta(api_basemodels.Style.Meta):
        verbose_name = "liquor-style"
        verbose_name_plural = "liquor-styles"
    
    liquor = models.ForeignKey(Liquor)
    
    def get_absolute_url(self):
        return reverse('style_retrieve_update_destroy', 
                       kwargs={'style':get_class_name(self._meta.verbose_name_plural), 
                       'style_id':str(self.id)})
# /LiquorStyle
admin.site.register(LiquorStyle)


class BeerReview(api_basemodels.Review):
    
    class Meta(api_basemodels.Review.Meta):
        verbose_name = "beer-review"
        verbose_name_plural = "beer-reviews"
    
    drink = models.ForeignKey(Beer)
    
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
        beer_reviews = BeerReview.objects.filter(beer=self.beer)
        aggregate_rating = sum([beer.total_rating for beer_review in beer_reviews])
        average_rating = aggregate_rating / beers.count()
        overall_beer_rating = round(DENOMINATOR * average_rating) / DENOMINATOR
        return overall_beer_rating
    
    def save(self, *args, **kwargs):
        """
        Pass a list of tuples of attributes and their respective rating weights.
        The weighted ratings are whole number percentages, so the sum of 
        weighted ratings must add up to 100.
        """
        self.total_rating = calculate_total_rating([(self.appearance, 10), 
                                                    (self.aroma, 25), 
                                                    (self.taste, 45), 
                                                    (self.palate, 15), 
                                                    (self.bottlestyle, 5)])
        super(BeerReview, self).save(*args, **kwargs)
        self.beer.overall_rating = calculate_overall_rating()
        super(BeerReview, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('review_retrieve_update_destroy', 
                       kwargs={'review':get_class_name(self._meta.verbose_name_plural), 
                       'review_id':str(self.id)})
# /BeerReview
admin.site.register(BeerReview)


class WineReview(api_basemodels.Review):
    
    class Meta(api_basemodels.Review.Meta):
        verbose_name = "wine-review"
        verbose_name_plural = "wine-reviews"
    
    drink = models.ForeignKey(Wine)
    
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
        wine_reviews = WineReview.objects.filter(wine=self.wine)
        aggregate_rating = sum([wine.total_rating for wine_review in wine_reviews])
        average_rating = aggregate_rating / wines.count()
        overall_wine_rating = round(DENOMINATOR * average_rating) / DENOMINATOR
        return overall_wine_rating
    
    def save(self, *args, **kwargs):
        """
        Pass a list of tuples of attributes and their respective rating weights.
        The weighted ratings are whole number percentages, so the sum of 
        weighted ratings must add up to 100.
        """
        self.total_rating = calculate_total_rating([(self.clarity, 5), 
                                                    (self.color, 5), 
                                                    (self.intensity, 5), 
                                                    (self.aroma, 20), 
                                                    (self.body, 5), 
                                                    (self.astringency, 5), 
                                                    (self.alcohol, 5), 
                                                    (self.balance, 15), 
                                                    (self.finish, 15), 
                                                    (self.complexity, 15), 
                                                    (self.bottlestyle, 5)])
        super(WineReview, self).save(*args, **kwargs)
        self.wine.overall_rating = calculate_overall_rating()
        super(WineReview, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('review_retrieve_update_destroy', 
                       kwargs={'review':get_class_name(self._meta.verbose_name_plural), 
                       'review_id':str(self.id)})
# /WineReview
admin.site.register(WineReview)


class LiquorReview(api_basemodels.Review):
    
    class Meta(api_basemodels.Review.Meta):
        verbose_name = "liquor-review"
        verbose_name_plural = "liquor-reviews"
    
    drink = models.ForeignKey(Liquor)
    
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
        liquor_reviews = LiquorReview.objects.filter(liquor=self.liquor)
        aggregate_rating = sum([liquor.total_rating for liquor_review in liquor_reviews])
        average_rating = aggregate_rating / liquors.count()
        overall_liquor_rating = round(DENOMINATOR * average_rating) / DENOMINATOR
        return overall_liquor_rating
    
    def save(self, *args, **kwargs):
        """
        Pass a list of tuples of attributes and their respective rating weights.
        The weighted ratings are whole number percentages, so the sum of 
        weighted ratings must add up to 100.
        """
        self.total_rating = calculate_total_rating([(self.appearance, 10), 
                                                    (self.aroma, 30), 
                                                    (self.taste, 45), 
                                                    (self.aftertaste, 15)])
        super(LiquorReview, self).save(*args, **kwargs)
        self.liquor.overall_rating = calculate_overall_rating()
        super(LiquorReview, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('review_retrieve_update_destroy', 
                       kwargs={'review':get_class_name(self._meta.verbose_name_plural), 
                       'review_id':str(self.id)})
# /LiquorReview
admin.site.register(LiquorReview)


# EOF - publican_api models
