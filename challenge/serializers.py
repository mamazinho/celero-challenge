from challenge.models import Athlete, AthleteInfo, Event, EventInfo
from rest_framework import serializers

class AthleteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AthleteInfo
        fields = '__all__'

class EventInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventInfo
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    event_infos = EventInfoSerializer(read_only=True, many=True)
    athlete_infos = AthleteInfoSerializer(many=True)

    class Meta:
        model = Event
        fields = '__all__'

class AthleteSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True)
    athlete_infos = AthleteInfoSerializer(read_only=True, many=True)
    class Meta:
        model = Athlete
        fields = '__all__'
