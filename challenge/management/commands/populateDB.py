from challenge.models import Athlete, AthleteInfo, Event
from django.core.management.base import BaseCommand
import datetime, json, requests, csv

'''
    This command get the csv from utils folder and save in respectives tables on database
'''
 
class Command(BaseCommand):

    def __instance_file(self):
        csv_file = open('challenge/utils/athlete_events.csv')
        reader = csv.DictReader(csv_file, delimiter=',')
        return reader

    def __check_line_value(self, line):
        for features in ['Age', 'Height', 'Weight', 'Medal']:
            line[features] = None if line[features] == 'NA' else line[features]
        return line

    def __save_data(self, line):
        athlete = self.__create_athlete(line)
        event = self.__create_event(line)
        athlete_info = self.__create_athlete_info(line, athlete)
        athlete_info.event.add(event)


    def __create_athlete(self, line):
        athlete, created = Athlete.objects.get_or_create(
            athlete_name=line['Name'].lstrip(),
        )
        return athlete

    def __create_event(self, line):
        event, created = Event.objects.get_or_create(
            event_name=line['Event'].lstrip(),
            city=line['City'],
            sport=line['Sport'],
            season=line['Season'],
            year=line['Year'],
            games=line['Games'],
        )
        return event

    def __create_athlete_info(self, line, athlete):
        athlete_info, created = AthleteInfo.objects.get_or_create(
            athlete=athlete,
            sex=line['Sex'],
            age=line['Age'],
            height=line['Height'],
            weight=line['Weight'],
            team=line['Team'],
            medal=line['Medal'],
        )
        return athlete_info


    def handle(self, *args, **options):

        # Get local csv
        reader = self.__instance_file()

        print("Reading CSV file...\n")
        for i, line in enumerate(reader):
            
            print(f'{i}/271116', end='\r', flush=True)
            line = self.__check_line_value(line)
            self.__save_data(line)
            
        print("Process completed successfully")