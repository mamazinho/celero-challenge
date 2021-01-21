from challenge.models import Athlete, AthleteInfo
from rest_framework import serializers
from .event_serializer import EventSerializer

class AthleteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AthleteInfo
        fields = '__all__'

class AthleteSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True)
    athlete_infos = AthleteInfoSerializer(read_only=True, many=True)
    class Meta:
        model = Athlete
        fields = '__all__'
