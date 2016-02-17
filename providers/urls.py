from django.conf.urls import url, include
from providers.views import (
    ProviderViewSet, ServiceAreaViewSet, SearchServiceAreaView)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'providers', ProviderViewSet)
router.register(r'serviceareas', ServiceAreaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^search/', SearchServiceAreaView.as_view())
]
