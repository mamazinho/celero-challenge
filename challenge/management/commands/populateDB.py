from challenge.models import Athlete, AthleteInfo, Event
from django.core.management.base import BaseCommand
import datetime, json, requests, csv

'''
    This command get the csv from utils folder and save in respectives tables on database
'''
 
class Command(BaseCommand):

    def handle(self, *args, **options):

        # Get local csv
        csv_file = open('challenge/utils/athlete_events.csv')
        reader = csv.DictReader(csv_file, delimiter=',')

        # Reading each csv line
        print("Reading CSV file...\n")
        for i, line in enumerate(reader):
            
            print(i)
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

        print("Process completed successfully")