from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from providers.models import Provider, ServiceArea


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    """
    Serializer to return GeoJSON compatible format

    https://github.com/djangonauts/django-rest-framework-gis#geofeaturemodelserializer
    """
    class Meta:
        model = ServiceArea
        geo_field = 'polygon'
