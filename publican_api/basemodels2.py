"""publican_api base models"""

from django.db import models
from django.utils.text import slugify

import publican_api.utils as api_utils


class Favorite(models.Model):
    
    class Meta:
        abstract = True
# /Favoriteable


class Drink(models.Model):
    
    class Meta:
        abstract = True
        app_label = api_utils.get_app_label()
        get_latest_by = "created"
    
    name = models.CharField("Name", 
                            max_length=128, 
                            unique=True, 
                            help_text="Max 128 characters.")
    
    slug = models.SlugField(max_length=128, 
                            editable=False)
    
    overall_rating = models.FloatField("Overall Rating", 
                                       null=True, 
                                       editable=False)
    
    favorite_of = models.ManyToManyField('auth.User', 
                                         related_name="%(app_label)s_%(class)s_favorite", 
                                         null=True)
    
    created = models.DateTimeField("Created", 
                                   auto_now_add=True, 
                                   editable=False)

    updated = models.DateTimeField("Updated", 
                                   auto_now=True, 
                                   editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Drink, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
# /Drink


class Facility(models.Model):
    
    class Meta:
        abstract = True
        app_label = api_utils.get_app_label()
        get_latest_by = "created"
    
    name = models.CharField("Name", 
                            max_length=128, 
                            unique=True, 
                            help_text="Max 128 characters.")
    
    slug = models.SlugField(max_length=128, 
                            editable=False)
    
    location = models.CharField("Location", 
                                max_length=128, 
                                help_text="Max 128 characters.")
    
    favorite_of = models.ManyToManyField('auth.User', 
                                         related_name="%(app_label)s_%(class)s_favorite", 
                                         null=True)
    
    created = models.DateTimeField("Created", 
                                   auto_now_add=True, 
                                   editable=False)

    updated = models.DateTimeField("Updated", 
                                   auto_now=True, 
                                   editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Facility, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
# /Facility


class Glass(models.Model):
    
    class Meta:
        abstract = True
        app_label = api_utils.get_app_label()
        get_latest_by = "created"
    
    name = models.CharField("Name", 
                            max_length=128, 
                            unique=True, 
                            help_text="Max 128 characters.")
    
    type = models.CharField(max_length=128, 
                            help_text="Max 128 characters.")
    
    slug = models.SlugField(max_length=128, 
                            editable=False)
    
    favorite_of = models.ManyToManyField('auth.User', 
                                         related_name="%(app_label)s_%(class)s_favorite", 
                                         null=True)
    
    created = models.DateTimeField("Created", 
                                   auto_now_add=True, 
                                   editable=False)

    updated = models.DateTimeField("Updated", 
                                   auto_now=True, 
                                   editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Glass, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
# /Glass


class Style(models.Model):
    
    class Meta:
        abstract = True
        app_label = api_utils.get_app_label()
        get_latest_by = "created"
    
    name = models.CharField(max_length=128, 
                            unique=True, 
                            help_text="Max 128 characters.")
    
    slug = models.SlugField(max_length=128, 
                            editable=False)
    
    favorite_of = models.ManyToManyField('auth.User', 
                                         related_name="%(app_label)s_%(class)s_favorite", 
                                         null=True)
    
    created = models.DateTimeField("Created", 
                                   auto_now_add=True, 
                                   editable=False)

    updated = models.DateTimeField("Updated", 
                                   auto_now=True, 
                                   editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Style, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
# /Style


class Review(models.Model):
    
    class Meta:
        abstract = True
        app_label = api_utils.get_app_label()
        get_latest_by = "created"
    
    DENOMINATOR = 4
    
    rater = models.ForeignKey('auth.User', 
                              related_name="%(app_label)s_%(class)s_rater")
    
    title = models.CharField(max_length=128, 
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
    
    def calculate_total_rating(self, categories):
        """
        1) Multiply rating by weighted value to determine weighted rating values.
            weighted_ratings = [category[0] * category[1] for category in categories]
        2) Sum the elements of weighted rating list.
            summed_ratings = sum(weighted_ratings)
        3) Divide summed ratings by 100 to get averaged rating.
            fractional_rating = summed_ratings / 100
        4) Ratchet fractional_rating to final quarter fractional value.
            total_rating = round(DENOMINATOR * fractional_rating) / DENOMINATOR
        5) Return total rating for this particular review.
        """
        #return (round(4 * (sum([c[0] * c[1] for c in categories]) / 100)) / 4)
        weighted_ratings = [category[0] * category[1] for category in categories]
        summed_ratings = sum(weighted_ratings)
        fractional_rating = summed_ratings / 100
        total_rating = round(DENOMINATOR * fractional_rating) / DENOMINATOR
        return total_rating
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Review, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
# /Review


# EOF - publican_api base models
