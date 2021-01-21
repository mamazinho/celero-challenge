from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from challenge.models import Event
from challenge.serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()