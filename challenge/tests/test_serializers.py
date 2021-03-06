from django.test import TestCase
from challenge.models import Athlete, AthleteInfo, Event
from challenge.serializers import AthleteInfoSerializer, AthleteSerializer, EventSerializer, EventOnlySerializer, AthleteNewInfoSerializer

class ModelsTest(TestCase):

    def setUp(self):
        self.athlete = Athlete.objects.create(
            athlete_name = 'Matheus'
        )
        self.athlete_info = AthleteInfo.objects.create(
            athlete = self.athlete,
            sex = 'M',
            age = 20,
            height = 1.76,
            weight = 60,
            team = 'Brasil',
            medal = 'Gold'
        )
        self.event = Event.objects.create(
            event_name = 'olympics',
            city = 'Curitiba',
            sport = 'parkour',
            season = 'Summer',
            year = 2020,
            games = '2020 Summer'
        )

        self.athlete_info.event.set([self.event.id])

    def test_event_serializer(self):
        serializer = EventSerializer(instance=self.event)
        self.assertEqual(serializer.data['city'], 'Curitiba')

    def test_event_only_serializer(self):
        serializer = EventOnlySerializer(instance=self.event)
        self.assertEqual(serializer.data['event_name'], 'olympics')
        
    def test_athlete_info_serializer(self):
        serializer = AthleteInfoSerializer(instance=self.athlete_info)
        self.assertEqual(serializer.data['age'], 20)

    def test_athlete_new_info_serializer(self):
        serializer = AthleteNewInfoSerializer(instance=self.athlete_info)
        self.assertEqual(serializer.data['weight'], 60)

    def test_athlete_serializer(self):
        serializer = AthleteSerializer(instance=self.athlete)
        self.assertEqual(serializer.data['athlete_name'], 'Matheus')