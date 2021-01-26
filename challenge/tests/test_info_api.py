from rest_framework.test import APITestCase
from rest_framework import status

class AthleteAPITest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.create_athlete = {
            'athlete_name': 'Matheus'
        }
        cls.create_infos = {
            'athlete': 1,
            'sex': 'M',
            'age': 20,
            'height': 1.75,
            'weight': 50,
            'team': 'Athletico',
            'medal': 'Gold',
            'event': [1]
        }
        cls.edit_info = {
            'id': 1,
            'age': 21,
            'height': 1.76,
            'weight': 60,
        }
        cls.create_events = {
            'event_name': 'olympics',
            'city': 'Curitiba',
            'sport': 'parkour',
            'year': 2020,
            'season': 'Summer',
            'games': '2020 Summer',
        }

    def test_get_info_api(self):
        response = self.client.get('/api/athletes-infos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_info_result_length_empty(self):
        response = self.client.get('/api/athletes-infos/')
        json = response.json()
        self.assertEqual(len(json), 0)

    def test_post_info_api(self):
        response = self.__create_info()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_info_result_length_empty_offset(self):
        response = self.client.get('/api/athletes-infos/?limit=1&limitoffset=20')
        json = response.json()['results']
        self.assertEqual(len(json), 0)

    def test_info_result_length_fill_offset(self):
        self.__create_info()
        response = self.client.get('/api/athletes-infos/?limit=1&limitoffset=20')
        json = response.json()['results']
        self.assertEqual(len(json), 1)

    def test_patch_info_api(self):
        response = self.__create_info()
        id = response.json()['id']
        response = self.client.patch(f'/api/athletes-infos/{id}/', self.edit_info)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def __create_info(self):
        athlete = self.client.post('/api/athletes/', self.create_athlete)
        athlete_id = athlete.json()['id']
        event = self.client.post('/api/events/', self.create_events)
        event_id = [event.json()['id']]
        self.create_infos['athlete'] = athlete_id
        self.create_infos['event'] = event_id
        response = self.client.post('/api/athletes-infos/', self.create_infos)

        return response
