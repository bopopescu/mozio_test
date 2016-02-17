from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as gis_models
from django_languages.fields import LanguageField


class Provider(models.Model):
    """
    A service provider
    """
    ## Fields ##
    name = models.CharField(max_length=128)
    email = models.EmailField()
    # assuming international number, not specific format
    phone = models.CharField(max_length=16)
    language = LanguageField()
    # https://en.wikipedia.org/wiki/ISO_4217
    currency = models.CharField(max_length=3)

    ## Methods ##
    def __unicode__(self):
        return u'%s' % self.name


class ServiceArea(models.Model):
    """
    An area of service of a given Provider.
    """
    ## Fields ##
    provider = models.ForeignKey(Provider, related_name='service_areas')
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    polygon = gis_models.MultiPolygonField()  # allow sparse areas

    ## Methods ##
    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.provider)
