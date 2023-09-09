"""publican_api base models"""

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.contenttypes import generic
from django.utils.text import slugify


class Resource(models.Model):
    
    class Meta:
        abstract = True
        app_label = settings.APP_LABEL
        get_latest_by = "updated"
        ordering = ['name']
    
    name = models.CharField("Name", 
                            max_length=128, 
                            unique=True, 
                            help_text="Max 128 characters.")
    
    slug = models.SlugField(max_length=128, 
                            editable=False)
    
    created = models.DateTimeField("Created", 
                                   auto_now_add=True, 
                                   editable=False)

    updated = models.DateTimeField("Updated", 
                                   auto_now=True, 
                                   editable=False)
    
    def get_absolute_url(self):
        _view_name = self._meta.verbose_name.replace(' ', '') + "-detail"
        return reverse(_view_name, kwargs={'lookup': str(self.id)})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Resource, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
# /Resource

        
class Drink(models.Model):
    
    class Meta:
        abstract = True
    
    overall_rating = models.FloatField("Overall Rating", 
                                       default=0, 
                                       editable=False)
# /Drink


class Facility(models.Model):
    
    class Meta:
        abstract = True

    location = models.CharField("Location", 
                                max_length=128, 
                                blank=False, 
                                help_text="Max 128 characters.")
# /Facility


class Glass(models.Model):
    
    class Meta:
        abstract = True
    
    type = models.CharField(max_length=128, 
                            blank=False, 
                            help_text="Max 128 characters.")
# /Glass


class Style(models.Model):
    
    class Meta:
        abstract = True
    
    description = models.CharField(max_length=128, 
                                   blank=False, 
                                   help_text="Max 128 characters.")
# /Style


class Review(models.Model):
    
    class Meta:
        abstract = True
        app_label = settings.APP_LABEL
        get_latest_by = "updated"
        ordering = ['title']
    
    rater = models.ForeignKey(User, 
                              related_name="%(app_label)s_%(class)s_rater")
    
    title = models.CharField(max_length=128, 
                             unique=True, 
                             help_text="Max 128 characters.")
    
    slug = models.SlugField(max_length=128, 
                            editable=False)
    
    description = models.CharField("Description", 
                                   max_length=1024, 
                                   blank=True)
    
    total_rating = models.FloatField("Total Rating", 
                                     default=0, 
                                     editable=False)
    
    created = models.DateTimeField("Created", 
                                   auto_now_add=True, 
                                   editable=False)

    updated = models.DateTimeField("Updated", 
                                   auto_now=True, 
                                   editable=False)
    
    @staticmethod
    def calculate_total_rating(categories):
        """
        1) Multiply rating by weighted value to determine weighted rating values.
            weighted_ratings = [category[0] * category[1] for category in categories]
        2) Sum the elements of weighted rating list.
            summed_ratings = sum(weighted_ratings)
        3) Divide summed ratings by 100 to get averaged rating.
            fractional_rating = summed_ratings / 100
        4) Ratchet fractional_rating to final quarter fractional value.
            total_rating = round(NUM_RATING_STARS * fractional_rating) / NUM_RATING_STARS
        5) Return total rating for this particular review.
        """
        DENOMINATION = 4
        
        #return (round(n * (sum([c[0] * c[1] for c in categories]) / 100)) / n)
        weighted_ratings = [category[0] * category[1] for category in categories]
        summed_ratings = sum(weighted_ratings)
        fractional_rating = summed_ratings / 100
        total_rating = round(DENOMINATION * fractional_rating) / DENOMINATION
        return total_rating
    
    def get_absolute_url(self):
        _view_name = self._meta.verbose_name.replace(' ', '') + "-detail"
        return reverse(_view_name, kwargs={'lookup': str(self.id)})
    
    def __str__(self):
        return self.title
# /Review


# EOF - publican_api base models
