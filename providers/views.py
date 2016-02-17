from rest_framework import viewsets
from rest_framework import generics
from django.contrib.gis.geos import Point

from providers.models import Provider, ServiceArea
from providers.serializers import (
    ProviderSerializer, ServiceAreaSerializer)


class ProviderViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Provider.objects.order_by('name')
    serializer_class = ProviderSerializer
    partial = True  # allow update with only changed data


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = ServiceArea.objects.order_by('name')
    serializer_class = ServiceAreaSerializer
    lookup_url_kwarg = 'servicearea_id'
    partial = True  # allow update with only changed data


class SearchServiceAreaView(generics.ListAPIView):
    serializer_class = ServiceAreaSerializer

    def get_queryset(self):
        """
        Returns the queryset of ServiceAreas that include the point
        given by `long` and `lat` parameters.
        """
        param_long = self.request.query_params.get('long', None)
        param_lat = self.request.query_params.get('lat', None)
        if param_long is None or param_lat is None:
            # longitude or latitud not given
            queryset = ServiceArea.objects.none()

        try:
            point_long = float(param_long)
            point_lat = float(param_lat)
            point = Point(point_lat, point_long)
            print dir(point)
            print point.json
            queryset = ServiceArea.objects.filter(polygon__contains=point)
        except (TypeError, ValueError):
            queryset = ServiceArea.objects.none()

        return queryset
