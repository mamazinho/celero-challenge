from challenge.models import Event, EventInfo
from rest_framework import serializers

class EventInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventInfo
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    event_infos = EventInfoSerializer(read_only=True, many=True)
    class Meta:
        model = Event
        fields = '__all__'