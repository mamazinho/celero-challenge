from django.urls import path, include
from rest_framework.routers import DefaultRouter
from challenge.views.api import *

router = DefaultRouter()

router.register(r'athletes', AthleteViewSet, basename='athletes')
router.register(r'athletes-infos', AthleteInfoViewSet, basename='athletes-infos')
router.register(r'events', EventViewSet, basename='events')


urlpatterns = router.urls