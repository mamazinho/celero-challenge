from challenge.models import Athlete, AthleteInfo, Event
from django.core.management.base import BaseCommand
import datetime, json, requests, csv, itertools
from multiprocessing.pool import ThreadPool
from random import randint
from time import sleep


'''
    This command get the csv from utils folder and save in respectives tables on database
'''
 
class Command(BaseCommand):
    i = 0
    def save_in_database(self, line):
        
        self.i+=1
        print(self.i)
        for features in ['Age', 'Height', 'Weight', 'Medal']:
            line[features] = None if line[features] == 'NA' else line[features]

        athlete, created = Athlete.objects.get_or_create(
            athlete_name=line['Name'].lstrip(),
        )

        event, created = Event.objects.get_or_create(
            event_name=line['Event'].lstrip(),
            city=line['City'],
            sport=line['Sport'],
            season=line['Season'],
            year=line['Year'],
            games=line['Games'],
        )

        athlete_info, created = AthleteInfo.objects.get_or_create(
            athlete=athlete,
            sex=line['Sex'],
            age=line['Age'],
            height=line['Height'],
            weight=line['Weight'],
            team=line['Team'],
            medal=line['Medal'],
        )
        athlete_info.event.add(event)


    def get_next_line(self, reader):
        for line in reader:
            yield line


    def handle(self, *args, **options):

        csv_file = open('challenge/utils/athlete_events.csv')
        reader = csv.DictReader(csv_file, delimiter=',')
        
        all_file = self.get_next_line(reader)
        thread = ThreadPool(processes=32)

        for line in all_file:
            thread.map(self.save_in_database, (line, ))

        thread.close()
        thread.join()