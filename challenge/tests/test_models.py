from django.test import TestCase
from challenge.models import Athlete, AthleteInfo, Event

class ModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.athlete = Athlete.objects.create(
            athlete_name = 'Matheus'
        )
        cls.athlete_info = AthleteInfo.objects.create(
            athlete = cls.athlete,
            sex = 'M',
            age = 20,
            height = 1.76,
            weight = 60,
            team = 'Brasil',
            medal = 'Gold'
        )
        cls.event = Event.objects.create(
            event_name = 'olympics',
            city = 'Curitiba',
            sport = 'parkour',
            season = 'Summer',
            year = '2020',
            games = '2020 Summer'
        )
        cls.athlete_info.event.set([cls.event.id])

    def test_athlete_model(self):
        record = Athlete.objects.all().first()
        self.assertEqual(record, self.athlete)
        
    def test_athlete_info_model(self):
        record = AthleteInfo.objects.all().first()
        self.assertEqual(record, self.athlete_info)

    def test_event_model(self):
        record = Event.objects.all().first()
        self.assertEqual(record, self.event)