from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from challenge.models import Event, EventInfo
from challenge.serializers import EventSerializer, EventInfoSerializer

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class EventInfoViewSet(viewsets.ModelViewSet):
    serializer_class = EventInfoSerializer
    queryset = EventInfo.objects.all()