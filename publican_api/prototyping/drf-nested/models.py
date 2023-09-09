"""drf-nested_api profiling models"""

from django.db import models


class Drink(models.Model):
    
    class Meta:
        get_latest_by = "created"
    
    name = models.CharField("Name", 
                            max_length=128, 
                            unique=True, 
                            help_text="Max 128 characters.")
    
    overall_rating = models.FloatField("Overall Rating")
    
    created = models.DateTimeField("Created", 
                                   auto_now_add=True, 
                                   editable=False)
    
    updated = models.DateTimeField("Updated", 
                                   auto_now=True, 
                                   editable=False)
    
    def __unicode__(self):
        return '%s' % (self.name)
# /Drink


class Glass(models.Model):
    
    class Meta:
        get_latest_by = "created"
    
    type = models.CharField(max_length=128, 
                            unique=True, 
                            help_text="Max 128 characters.")
    
    created = models.DateTimeField("Created", 
                                   auto_now_add=True, 
                                   editable=False)
    
    updated = models.DateTimeField("Updated", 
                                   auto_now=True, 
                                   editable=False)
    
    def __unicode__(self):
        return '%s' % (self.type)
# /Glass


# EOF