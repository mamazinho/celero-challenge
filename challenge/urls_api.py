from django.urls import path, include
from rest_framework.routers import DefaultRouter
from challenge.views.api import *

router = DefaultRouter()

router.register(r'athletes', AthleteViewSet, basename='athletes')
router.register(r'athletes_info', AthleteInfoViewSet, basename='athletes_info')
router.register(r'events', EventViewSet, basename='events')
router.register(r'events_info', EventInfoViewSet, basename='events_info')


urlpatterns = router.urls