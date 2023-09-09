"""beermeister models"""

from django.db import models
from django.utils.translation import ugettext_lazy as _


class TrackedClass(models.Model):
    class Meta:
        abstract = True
        get_latest_by = "created"
    
    created = models.DateTimeField(_("Created"), 
                                   auto_now_add=True, 
                                   editable=False)

    updated = models.DateTimeField(_("Updated"), 
                                   auto_now=True, 
                                   editable=False)
# /TrackedClass

class BeerBrewery(TrackedClass):
    
    class Meta:
        verbose_name_plural = "beer breweries"
    
    name = models.CharField(_("Name"), 
                            max_length=128, 
                            help_text=_("Max 128 characters."))
    
    location = models.CharField(_("Location"), 
                                max_length=128, 
                                help_text=_("Max 128 characters."))
    
    def __unicode__(self):
        return self.name
# /BeerBrewery


class BeerGlass(TrackedClass):
    
    class Meta:
        verbose_name_plural = "beer glasses"
    
    type = models.CharField(max_length=128, 
                            help_text=_("Max 128 characters."))
    
    def __unicode__(self):
        return self.type
# /BeerGlass


class BeerStyle(TrackedClass):
    
    style = models.CharField(max_length=128, 
                             help_text=_("Max 128 characters."))
    
    def __unicode__(self):
        return self.name
# /BeerStyle

    
class Beer(TrackedClass):
    
    name = models.CharField(_("Name"), 
                            max_length=128, 
                            help_text=_("Max 128 characters."))
        
    ibu = models.PositiveSmallIntegerField(_("International Bitterness Units"))
    # range: 5-100
    
    calories = models.PositiveSmallIntegerField(_("Calories"))
    # range: 50-1000
    
    abv = models.FloatField(_("Alcohol By Volume"))
    # range: 0-80
    
    brewery = models.ForeignKey(BeerBrewery, 
                                verbose_name=_("Beer Brewery"))
    
    glass = models.ForeignKey(BeerGlass, 
                              verbose_name=_("Beer Glass"))
    
    style = models.ForeignKey(BeerStyle, 
                              verbose_name=_("Beer Style"))
    
    def __unicode__(self):
        return self.name
# /Beer


class BeerReview(TrackedClass):
    
    beer = models.ForeignKey(Beer)
    
    rater = models.ForeignKey('auth.User')
    
    aroma = models.PositiveSmallIntegerField(_("Aroma"), 
                                             default=0)
    # range: 1-5
    
    appearance = models.PositiveSmallIntegerField(_("Appearance"), 
                                                  default=0)
    # range: 1-5
    
    taste = models.PositiveSmallIntegerField(_("Taste"), 
                                             default=0)
    # range: 1-10
    
    palate = models.PositiveSmallIntegerField(_("Palate"), 
                                              default=0)
    # range: 1-5
    
    bottlestyle = models.PositiveSmallIntegerField(_("Bottle Style"), 
                                                   default=0)
    # range: 1-5
    
    description = models.TextField(_("Description"), 
                                   blank=True)
    
    rating = models.FloatField(_("Rating"), 
                               editable=False)
    
    def __unicode__(self):
        return self.beer.name
# /BeerReview


class FavoriteBeerBrewery(TrackedClass):
    
    class Meta:
        verbose_name_plural = "favorite beer breweries"
    
    beerbrewery = models.ForeignKey(BeerBrewery)
    
    admirer = models.ForeignKey('auth.User', 
                                related_name='fave_beerbrewery')
    
    def __unicode__(self):
        return self.beerbrewery.name
# /FavoriteBrewery


class FavoriteBeerGlass(TrackedClass):
    
    class Meta:
        verbose_name_plural = "favorite beer glasses"
    
    beerglass = models.ForeignKey(BeerGlass)
    
    admirer = models.ForeignKey('auth.User', 
                                related_name='fave_beerglass')

    def __unicode__(self):
        return self.beerglass.type
# /FavoriteGlass


class FavoriteBeerStyle(TrackedClass):
    
    class Meta:
        verbose_name_plural = "favorite beer styles"
    
    beerstyle = models.ForeignKey(BeerStyle)
    
    admirer = models.ForeignKey('auth.User', 
                                related_name='fave_beerstyle')

    def __unicode__(self):
        return self.beerstyle.name
# /FavoriteBeerStyle


class FavoriteBeer(TrackedClass):
    
    class Meta:
        verbose_name_plural = "favorite beers"
    
    beer = models.ForeignKey(Beer)
    
    admirer = models.ForeignKey('auth.User', 
                                related_name='fave_beer')

    def __unicode__(self):
        return self.beer.name
# /FavoriteBeer


class ReadOnlyText(models.Model):
    
    class Meta:
        abstract = True
    
    latestversion = models.CharField(_("Latest Version"), 
                                     max_length=32, 
                                     help_text=_("Max 32 characters."))
    
    name = models.CharField(_("Name"), 
                            max_length=32, 
                            help_text=_("Max 32 characters."))
    
    contents = models.TextField(_("Contents"))
    
    created = models.DateTimeField(_("Created"), 
                                   auto_now_add=True, 
                                   editable=False)

    updated = models.DateTimeField(_("Updated"), 
                                   auto_now=True, 
                                   editable=False)
    
    def __unicode__(self):
        return self.latestversion
# /ReadOnlyText
        

class Document(ReadOnlyText):
    pass
# /Documentation


class SourceCode(ReadOnlyText):
    
    class Meta:
        verbose_name_plural = "source code"
# /SourceCode


# EOF - beermeister models.py