from challenge.models import Event, AthleteInfo, Athlete
from rest_framework import serializers

class EventAthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = '__all__'

class EventInfoAthleteSerializer(serializers.ModelSerializer):
    athlete = EventAthleteSerializer(read_only=True)

    class Meta:
        model = AthleteInfo
        fields = ['id', 'athlete', 'age', 'height', 'weight', 'medal', 'team', 'sex']
    
class EventSerializer(serializers.ModelSerializer):
    athlete_infos = EventInfoAthleteSerializer(read_only=True, many=True)
    class Meta:
        model = Event
        fields = '__all__'

class EventSerializerOnly(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'