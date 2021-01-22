from challenge.models import Athlete, AthleteInfo, Event, EventInfo
from django.core.management.base import BaseCommand
import datetime, json, requests, csv

'''
    This command get the csv from utils folder and save in respectives tables on database
'''
 
class Command(BaseCommand):

    def handle(self, *args, **options):

        # Get local csv
        csv_file = open('challenge/utils/athlete_events.csv')
        to_create = []
        reader = csv.DictReader(csv_file, delimiter=',')

        # Reading each csv line
        print("Reading CSV file...\n")
        for line in reader:

            event, created = Event.objects.get_or_create(
                event_name=line['Event']
            )

            event_info, created = EventInfo.objects.get_or_create(
                event=event,
                city=line['City'],
                sport=line['Sport'],
                season=line['Season'],
                year=line['Year'],
                games=line['Games'],
            )

            athlete, created = Athlete.objects.get_or_create(
                athlete_name=line['Name'],
            )
            athlete.events.add(event)
            athlete.save()

            athlete_info, created = AthleteInfo.objects.get_or_create(
                athlete=athlete,
                sex=line['Sex'],
                age=line['Age'],
                height=line['Height'],
                weight=line['Weight'],
                team=line['Team'],
                medal=line['Medal'],
            )
            event.athlete_infos.add(athlete_info)
            athlete.save()
            
            print(f'{event}\n{event_info}\n{athlete}\n{athlete_info}')
            break

        # Save in database
        # Site.objects.bulk_create(to_create, ignore_conflicts=True)

        print("Process completed successfully")