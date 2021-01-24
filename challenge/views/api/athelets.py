from challenge.models import Athlete, AthleteInfo
from challenge.serializers import AthleteSerializer, AthleteInfoSerializer
from rest_framework import viewsets
from rest_framework.decorators import action

class AthleteViewSet(viewsets.ModelViewSet):
    serializer_class = AthleteSerializer
    queryset = Athlete.objects.all()

@action(methods=['post'], detail=True)
class AthleteInfoViewSet(viewsets.ModelViewSet):
    serializer_class = AthleteInfoSerializer
    queryset = AthleteInfo.objects.all()