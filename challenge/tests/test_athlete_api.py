from rest_framework.test import APITestCase
from rest_framework import status

class AthleteAPITest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.create_athlete = {
            'athlete_name': 'Matheus'
        }
        cls.edit_athlete = {
            'athlete_name': 'Math'
        }

    def test_get_athlete_api(self):
        response = self.client.get('/api/athletes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_athlete_result_length_empty(self):
        response = self.client.get('/api/athletes/')
        json = response.json()
        self.assertEqual(len(json), 0)

    def test_post_athlete_api(self):
        response = self.client.post('/api/athletes/', self.create_athlete)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_athlete_result_length_empty_offset(self):
        response = self.client.get('/api/athletes/?limit=1&limitoffset=20')
        json = response.json()['results']
        self.assertEqual(len(json), 0)

    def test_athlete_result_length_fill_offset(self):
        self.client.post('/api/athletes/', self.create_athlete)
        response = self.client.get('/api/athletes/?limit=1&limitoffset=20')
        json = response.json()['results']
        self.assertEqual(len(json), 1)

    def test_put_athlete_api(self):
        response = self.client.post('/api/athletes/', self.create_athlete)
        id = response.json()['id']
        response = self.client.put(f'/api/athletes/{id}/', self.edit_athlete)
        self.assertEqual(response.status_code, status.HTTP_200_OK)