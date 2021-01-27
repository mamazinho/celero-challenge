from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from challenge.models import Event
from challenge.serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        params = self.request.query_params
        if params and 'event_name' in params:
            event_name = params.get('event_name').title()
            queryset = Event.objects.filter(event_name__icontains=event_name)
        else:
            queryset = Event.objects.all()
        return queryset.order_by('-id')