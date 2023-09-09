"""publican_api models"""

from django.db import models
from django.core.urlresolvers import reverse

import publican_api.basemodels as api_basemodels
import publican_api.utils as api_utils


def get_class_name(verbose_name=None):
    return verbose_name.replace(" ", "")


class Beer(api_basemodels.Drink):
    
    class Meta(api_basemodels.Drink.Meta):
        verbose_name_plural = "beers"
    
    # range: 5-100
    ibu = models.PositiveSmallIntegerField("International Bitterness Units")
    
    # range: 50-1000
    calories = models.PositiveSmallIntegerField("Calories")
    
    # range: 0-80
    abv = models.FloatField("Alcohol By Volume")
    
    def get_absolute_url(self):
        return reverse('drink_retrieve_update_destroy', 
                       kwargs={'drink':get_class_name(self._meta.verbose_name),
                       'drink_id':str(self.id)})
# /Beer


class Wine(api_basemodels.Drink):
    
    class Meta(api_basemodels.Drink.Meta):
        verbose_name_plural = "wines"
    
    TANNIN_CHOICES = (
        ('L', 'Low'), 
        ('H', 'High'),
    )
    
    # range: 1-1000
    sweetness = models.PositiveSmallIntegerField("Sweetness")
    
    # range: 0.1-1.0
    acidity = models.FloatField("Acidity")
    
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
                       kwargs={'drink':get_class_name(self._meta.verbose_name), 
                       'drink_id':str(self.id)})
# /Wine


class Liquor(api_basemodels.Drink):
    
    class Meta(api_basemodels.Drink.Meta):
        verbose_name_plural = "liquors"
    
    # range: 0-80
    abv = models.FloatField("Alcohol By Volume")
    
    # range: 50-1000
    calories = models.PositiveSmallIntegerField("Calories")
    
    def get_absolute_url(self):
        return reverse('drink_retrieve_update_destroy', 
                       kwargs={'drink':get_class_name(self._meta.verbose_name), 
                       'drink_id':str(self.id)})
# /Liquor


class Brewery(api_basemodels.Facility):
    
    class Meta(api_basemodels.Facility.Meta):
        verbose_name_plural = "breweries"
    
    beer = models.ForeignKey(Beer)
    
    def get_absolute_url(self):
        return reverse('facility_retrieve_update_destroy', 
                       kwargs={'facility':get_class_name(self._meta.verbose_name), 
                       'facility_id':str(self.id)})
# /Brewery


class Winery(api_basemodels.Facility):
    
    class Meta(api_basemodels.Facility.Meta):
        verbose_name_plural = "wineries"
    
    wine = models.ForeignKey(Wine)
    
    def get_absolute_url(self):
        return reverse('facility_retrieve_update_destroy', 
                       kwargs={'facility':get_class_name(self._meta.verbose_name), 
                       'facility_id':str(self.id)})
# /Winery


class Distillery(api_basemodels.Facility):
    
    class Meta(api_basemodels.Facility.Meta):
        verbose_name_plural = "distilleries"
    
    liquor = models.ForeignKey(Liquor)
    
    def get_absolute_url(self):
        return reverse('facility_retrieve_update_destroy', 
                       kwargs={'facility':get_class_name(self._meta.verbose_name), 
                       'facility_id':str(self.id)})
# /Distillery


class BeerGlass(api_basemodels.Glass):
    
    class Meta(api_basemodels.Glass.Meta):
        verbose_name_plural = "beer glasses"
    
    beer = models.ForeignKey(Beer)
    
    def get_absolute_url(self):
        return reverse('glass_retrieve_update_destroy', 
                       kwargs={'glass':get_class_name(self._meta.verbose_name), 
                       'glass_id':str(self.id)})
# /BeerGlass


class WineGlass(api_basemodels.Glass):
    
    class Meta(api_basemodels.Glass.Meta):
        verbose_name_plural = "wine glasses"
    
    wine = models.ForeignKey(Wine)
    
    def get_absolute_url(self):
        return reverse('glass_retrieve_update_destroy', 
                       kwargs={'glass':get_class_name(self._meta.verbose_name), 
                       'glass_id':str(self.id)})
# /WineGlass


class LiquorGlass(api_basemodels.Glass):
    
    class Meta(api_basemodels.Glass.Meta):
        verbose_name_plural = "liquor glasses"
    
    liquor = models.ForeignKey(Liquor)
    
    def get_absolute_url(self):
        return reverse('glass_retrieve_update_destroy', 
                       kwargs={'glass':get_class_name(self._meta.verbose_name), 
                       'glass_id':str(self.id)})
# /LiquorGlass


class BeerStyle(api_basemodels.Style):
    
    class Meta(api_basemodels.Style.Meta):
        verbose_name_plural = "beer styles"
    
    beer = models.ForeignKey(Beer)
    
    def get_absolute_url(self):
        return reverse('style_retrieve_update_destroy', 
                       kwargs={'style':get_class_name(self._meta.verbose_name), 
                       'style_id':str(self.id)})
# /BeerStyle


class WineStyle(api_basemodels.Style):
    
    class Meta(api_basemodels.Style.Meta):
        verbose_name_plural = "wine styles"
    
    wine = models.ForeignKey(Wine)
    
    def get_absolute_url(self):
        return reverse('style_retrieve_update_destroy', 
                       kwargs={'style':get_class_name(self._meta.verbose_name), 
                       'style_id':str(self.id)})
# /WineStyle


class LiquorStyle(api_basemodels.Style):
    
    class Meta(api_basemodels.Style.Meta):
        verbose_name_plural = "liquor styles"
    
    liquor = models.ForeignKey(Liquor)
    
    def get_absolute_url(self):
        return reverse('style_retrieve_update_destroy', 
                       kwargs={'style':get_class_name(self._meta.verbose_name), 
                       'style_id':str(self.id)})
# /LiquorStyle


class BeerReview(api_basemodels.Review):
    
    class Meta(api_basemodels.Review.Meta):
        verbose_name_plural = "beer reviews"
    
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
                       kwargs={'review':get_class_name(self._meta.verbose_name), 
                       'review_id':str(self.id)})
# /BeerReview


class WineReview(api_basemodels.Review):
    
    class Meta(api_basemodels.Review.Meta):
        verbose_name_plural = "wine reviews"
    
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
                       kwargs={'review':get_class_name(self._meta.verbose_name), 
                       'review_id':str(self.id)})
# /WineReview


class LiquorReview(api_basemodels.Review):
    
    class Meta(api_basemodels.Review.Meta):
        verbose_name_plural = "liquor reviews"
    
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
                       kwargs={'review':get_class_name(self._meta.verbose_name), 
                       'review_id':str(self.id)})
# /LiquorReview


class InstallationDocument(api_basemodels.Document):
    
    class Meta:
        verbose_name_plural = "installation documents"

    def get_file_name(instance, filename):
        file_path = 'documents/install/'
        file_name = self._meta.verbose_name
        file_version = '_' + api_utils.get_api_version()
        return  file_path + file_name + file_version
    
    source_file = models.FileField(upload_to=get_file_name, 
                                   verbose_name="Source File")
    
    def read_source_file(self):
        try:
            file_contents = open(self.source_file, 'r')
        except PermissionError as err:
            print("File error({0}): {1}".format(err.errno, err.strerror))
        else:
            with file_contents:
                return file_contents.read() 
    
    def save(self, *args, **kwargs):
        self.name = self._meta.verbose_name.title()
        
        self.version = api_utils.get_api_version()
        
        super(InstallationDocument, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('document_retrieve_update_destroy', 
                       kwargs={'document':get_class_name(self._meta.verbose_name), 
                       'document_id':str(self.id)})
# /InstallationDocument


class ExecutionDocument(api_basemodels.Document):
    
    class Meta:
        verbose_name_plural = "execution documents"
    
    def get_file_name(instance, filename):
        file_path = 'documents/install/'
        file_name = self._meta.verbose_name
        file_version = '_' + api_utils.get_api_version()
        return  file_path + file_name + file_version
    
    source_file = models.FileField(upload_to=get_file_name, 
                                   verbose_name="Source File")
    
    def read_source_file(self):
        try:
            file_contents = open(self.source_file, 'r')
        except PermissionError as err:
            print("File error({0}): {1}".format(err.errno, err.strerror))
        else:
            with file_contents:
                return file_contents.read() 
    
    def save(self, *args, **kwargs):
        self.name = self._meta.verbose_name.title()
        
        self.version = api_utils.get_api_version()
        
        super(ExecutionDocument, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('document_retrieve_update_destroy', 
                       kwargs={'document':get_class_name(self._meta.verbose_name), 
                       'document_id':str(self.id)})
# /ExecutionDocument


class RequirementsDocument(api_basemodels.Document):
    
    class Meta:
        verbose_name_plural = "requirements documents"
    
    def get_file_name(instance, filename):
        file_path = 'documents/install/'
        file_name = self._meta.verbose_name
        file_version = '_' + api_utils.get_api_version()
        return  file_path + file_name + file_version
    
    source_file = models.FileField(upload_to=get_file_name, 
                                   verbose_name="Source File")
    
    def read_source_file(self):
        try:
            file_contents = open(self.source_file, 'r')
        except PermissionError as err:
            print("File error({0}): {1}".format(err.errno, err.strerror))
        else:
            with file_contents:
                return file_contents.read() 
    
    def save(self, *args, **kwargs):
        self.name = self._meta.verbose_name.title()
        
        self.version = api_utils.get_api_version()
        
        super(RequirementsDocument, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('document_retrieve_update_destroy', 
                       kwargs={'document':get_class_name(self._meta.verbose_name), 
                       'document_id':str(self.id)})
# /RequirementsDocument


class DefinitionsDocument(api_basemodels.Document):
    
    class Meta:
        verbose_name_plural = "definitions document"
    
    def get_file_name(instance, filename):
        file_path = 'documents/install/'
        file_name = self._meta.verbose_name
        file_version = '_' + api_utils.get_api_version()
        return  file_path + file_name + file_version
    
    source_file = models.FileField(upload_to=get_file_name, 
                                   verbose_name="Source File")
    
    def read_source_file(self):
        try:
            file_contents = open(self.source_file, 'r')
        except PermissionError as err:
            print("File error({0}): {1}".format(err.errno, err.strerror))
        else:
            with file_contents:
                return file_contents.read() 
    
    def save(self, *args, **kwargs):
        self.name = self._meta.verbose_name.title()
        
        self.version = api_utils.get_api_version()
        
        super(DefinitionsDocument, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('document_retrieve_update_destroy', 
                       kwargs={'document':get_class_name(self._meta.verbose_name), 
                       'document_id':str(self.id)})
# /DefinitionsDocument


class BaseModelsDocument(api_basemodels.Document):
    
    class Meta:
        verbose_name_plural = "basemodels document"
    
    def get_file_name(instance, filename):
        file_path = 'documents/install/'
        file_name = self._meta.verbose_name
        file_version = '_' + api_utils.get_api_version()
        return  file_path + file_name + file_version
    
    source_file = models.FileField(upload_to=get_file_name, 
                                   verbose_name="Source File")
    
    def read_source_file(self):
        try:
            file_contents = open(self.source_file, 'r')
        except PermissionError as err:
            print("File error({0}): {1}".format(err.errno, err.strerror))
        else:
            with file_contents:
                return file_contents.read() 
    
    def save(self, *args, **kwargs):
        self.name = self._meta.verbose_name.title()
        
        self.version = api_utils.get_api_version()
        
        super(BaseModelsDocument, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('document_retrieve_update_destroy', 
                       kwargs={'document':get_class_name(self._meta.verbose_name), 
                       'document_id':str(self.id)})
# /BaseModelsDocument


class ModelsDocument(api_basemodels.Document):
    
    class Meta:
        verbose_name_plural = "models documents"
    
    def get_file_name(instance, filename):
        file_path = 'documents/install/'
        file_name = self._meta.verbose_name
        file_version = '_' + api_utils.get_api_version()
        return  file_path + file_name + file_version
    
    source_file = models.FileField(upload_to=get_file_name, 
                                   verbose_name="Source File")
    
    def read_source_file(self):
        try:
            file_contents = open(self.source_file, 'r')
        except PermissionError as err:
            print("File error({0}): {1}".format(err.errno, err.strerror))
        else:
            with file_contents:
                return file_contents.read() 
    
    def save(self, *args, **kwargs):
        self.name = self._meta.verbose_name.title()
        
        self.version = api_utils.get_api_version()
        
        super(ModelsDocument, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('document_retrieve_update_destroy', 
                       kwargs={'document':get_class_name(self._meta.verbose_name), 
                       'document_id':str(self.id)})
# /ModelsDocument


class ViewsDocument(api_basemodels.Document):
    
    class Meta:
        verbose_name_plural = "views documents"
    
    def get_file_name(instance, filename):
        file_path = 'documents/install/'
        file_name = self._meta.verbose_name
        file_version = '_' + api_utils.get_api_version()
        return  file_path + file_name + file_version
    
    source_file = models.FileField(upload_to=get_file_name, 
                                   verbose_name="Source File")
    
    def read_source_file(self):
        try:
            file_contents = open(self.source_file, 'r')
        except PermissionError as err:
            print("File error({0}): {1}".format(err.errno, err.strerror))
        else:
            with file_contents:
                return file_contents.read() 
    
    def save(self, *args, **kwargs):
        self.name = self._meta.verbose_name.title()
        
        self.version = api_utils.get_api_version()
        
        super(ViewsDocument, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('document_retrieve_update_destroy', 
                       kwargs={'document':get_class_name(self._meta.verbose_name), 
                       'document_id':str(self.id)})
# /ViewsDocument


class SerializersDocument(api_basemodels.Document):
    
    class Meta:
        verbose_name_plural = "serializers documents"
    
    def get_file_name(instance, filename):
        file_path = 'documents/install/'
        file_name = self._meta.verbose_name
        file_version = '_' + api_utils.get_api_version()
        return  file_path + file_name + file_version
    
    source_file = models.FileField(upload_to=get_file_name, 
                                   verbose_name="Source File")
    
    def read_source_file(self):
        try:
            file_contents = open(self.source_file, 'r')
        except PermissionError as err:
            print("File error({0}): {1}".format(err.errno, err.strerror))
        else:
            with file_contents:
                return file_contents.read() 
    
    def save(self, *args, **kwargs):
        self.name = self._meta.verbose_name.title()
        
        self.version = api_utils.get_api_version()
        
        super(SerializersDocument, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('document_retrieve_update_destroy', 
                       kwargs={'document':get_class_name(self._meta.verbose_name), 
                       'document_id':str(self.id)})
# /SerializersDocument


class ThrottlesDocument(api_basemodels.Document):
    
    class Meta:
        verbose_name_plural = "throttles documents"
    
    def get_file_name(instance, filename):
        file_path = 'documents/install/'
        file_name = self._meta.verbose_name
        file_version = '_' + api_utils.get_api_version()
        return  file_path + file_name + file_version
    
    source_file = models.FileField(upload_to=get_file_name, 
                                   verbose_name="Source File")
    
    def read_source_file(self):
        try:
            file_contents = open(self.source_file, 'r')
        except PermissionError as err:
            print("File error({0}): {1}".format(err.errno, err.strerror))
        else:
            with file_contents:
                return file_contents.read() 
    
    def save(self, *args, **kwargs):
        self.name = self._meta.verbose_name.title()
        
        self.version = api_utils.get_api_version()
        
        super(ThrottlesDocument, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('document_retrieve_update_destroy', 
                       kwargs={'document':get_class_name(self._meta.verbose_name), 
                       'document_id':str(self.id)})
# /ThrottlesDocument


class PermissionsDocument(api_basemodels.Document):
    
    class Meta:
        verbose_name_plural = "permissions documents"
    
    def get_file_name(instance, filename):
        file_path = 'documents/install/'
        file_name = self._meta.verbose_name
        file_version = '_' + api_utils.get_api_version()
        return  file_path + file_name + file_version
    
    source_file = models.FileField(upload_to=get_file_name, 
                                   verbose_name="Source File")
    
    def read_source_file(self):
        try:
            file_contents = open(self.source_file, 'r')
        except PermissionError as err:
            print("File error({0}): {1}".format(err.errno, err.strerror))
        else:
            with file_contents:
                return file_contents.read() 
    
    def save(self, *args, **kwargs):
        self.name = self._meta.verbose_name.title()
        
        self.version = api_utils.get_api_version()
        
        super(PermissionsDocument, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('document_retrieve_update_destroy', 
                       kwargs={'document':get_class_name(self._meta.verbose_name), 
                       'document_id':str(self.id)})
# /PermissionsDocument


# EOF - publican_api models
