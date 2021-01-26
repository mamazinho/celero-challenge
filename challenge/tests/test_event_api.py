from rest_framework.test import APITestCase
from rest_framework import status

class AthleteAPITest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.create_events = {
            'event_name': 'olympics',
            'city': 'Curitiba',
            'sport': 'parkour',
            'year': 2020,
            'season': 'Summer',
            'games': '2020 Summer',
        }
        cls.edit_event = {
            'id': 1,
            'event_name': 'olympics',
            'city': 'Curitiba',
            'sport': 'parkour',
            'year': 2021,
            'season': 'Winter',
            'games': '2020 Winter',
        }
        cls.patch_event = {
            'id': 1,
            'event_name': 'olympics',
            'city': 'Londres',
            'sport': 'parkour',
            'year': 2022,
            'season': 'Autumn',
            'games': '2022 Autumn',
        }

    def test_get_event_api(self):
        response = self.client.get('/api/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_event_result_length_empty(self):
        response = self.client.get('/api/events/')
        json = response.json()
        self.assertEqual(len(json), 0)

    def test_post_event_api(self):
        response = self.client.post('/api/events/', self.create_events)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_event_result_length_empty_offset(self):
        response = self.client.get('/api/events/?limit=1&limitoffset=20')
        json = response.json()['results']
        self.assertEqual(len(json), 0)

    def test_event_result_length_fill_offset(self):
        self.client.post('/api/events/', self.create_events)
        response = self.client.get('/api/events/?limit=1&limitoffset=20')
        json = response.json()['results']
        self.assertEqual(len(json), 1)

    def test_put_event_api(self):
        response = self.client.post('/api/events/', self.create_events)
        id = response.json()['id']
        response = self.client.put(f'/api/events/{id}/', self.edit_event)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_event_api(self):
        response = self.client.post('/api/events/', self.create_events)
        id = response.json()['id']
        response = self.client.patch(f'/api/events/{id}/', self.patch_event)
        self.assertEqual(response.status_code, status.HTTP_200_OK)