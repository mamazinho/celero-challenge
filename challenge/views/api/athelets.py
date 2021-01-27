from challenge.models import Athlete, AthleteInfo
from challenge.serializers import AthleteSerializer, AthleteInfoSerializer, AthleteNewInfoSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from django.db.models import Q

class AthleteViewSet(viewsets.ModelViewSet):
    serializer_class = AthleteSerializer

    def get_queryset(self):
        params = self.request.query_params
        if params and 'athlete_name' in params:
            athlete_name = params.get('athlete_name').title()
            queryset = Athlete.objects.filter(athlete_name__icontains=athlete_name)
        else:
            queryset = Athlete.objects.all()
        return queryset

class AthleteInfoViewSet(viewsets.ModelViewSet):
    queryset = AthleteInfo.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return AthleteNewInfoSerializer

        return AthleteInfoSerializer