from challenge.models import Athlete, AthleteInfo
from challenge.serializers import AthleteSerializer
from rest_framework import viewsets


class AthleteViewSet(viewsets.ModelViewSet):
    serializer_class = AthleteSerializer
    queryset = Athlete.objects.all()