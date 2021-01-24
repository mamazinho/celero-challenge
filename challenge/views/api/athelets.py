from challenge.models import Athlete, AthleteInfo
from challenge.serializers import AthleteSerializer, AthleteInfoSerializer, AthleteNewInfoSerializer
from rest_framework import viewsets
from rest_framework.decorators import action

class AthleteViewSet(viewsets.ModelViewSet):
    serializer_class = AthleteSerializer
    queryset = Athlete.objects.all()

class AthleteInfoViewSet(viewsets.ModelViewSet):
    queryset = AthleteInfo.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return AthleteNewInfoSerializer

        return AthleteInfoSerializer