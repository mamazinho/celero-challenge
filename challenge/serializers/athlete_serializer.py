from challenge.models import Athlete, AthleteInfo, Event
from rest_framework import serializers
from .event_serializer import EventOnlySerializer

class AthleteInfoSerializer(serializers.ModelSerializer):
    event = EventOnlySerializer(read_only=True, many=True)

    class Meta:
        model = AthleteInfo
        fields = '__all__'
    
class AthleteNewInfoSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), many=True)

    class Meta:
        model = AthleteInfo
        fields = '__all__'

class AthleteSerializer(serializers.ModelSerializer):
    athlete_infos = AthleteInfoSerializer(read_only=True, many=True)
    class Meta:
        model = Athlete
        fields = '__all__'
