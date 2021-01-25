from challenge.models import Athlete, AthleteInfo, Event
from django.core.management.base import BaseCommand
import datetime, json, requests, csv, random

'''
    This command get the csv from utils folder and save in respectives tables on database
'''
 
class Command(BaseCommand):

    def handle(self, *args, **options):

        # Get local csv
        csv_file = open('challenge/utils/athlete_events.csv')
        reader = csv.DictReader(csv_file, delimiter=',')

        to_create_ath = []
        to_create_eve = []
        to_create_ati = []

        # Reading each csv line
        print("Reading CSV file...\n")
        for index, line in enumerate(reader):
            print(index)
            # for features in ['Age', 'Height', 'Weight', 'Medal']:
            #     line[features] = None if line[features] == 'NA' else line[features]
            line['Age'] = None if line['Age'] == 'NA' else line['Age']
            line['Height'] = None if line['Height'] == 'NA' else line['Height']
            line['Weight'] = None if line['Weight'] == 'NA' else line['Weight']
            line['Medal'] = None if line['Medal'] == 'NA' else line['Medal']

            ath = Athlete(
                athlete_name=line['Name'].lstrip(),
            )

            eve = Event(
                event_name=line['Event'].lstrip(),
                city=line['City'],
                sport=line['Sport'],
                season=line['Season'],
                year=line['Year'],
                games=line['Games'],
            )

            ati = AthleteInfo(
                athlete=ath,
                sex=line['Sex'],
                age=line['Age'],
                height=line['Height'],
                weight=line['Weight'],
                team=line['Team'],
                medal=line['Medal'],
            )

            if ath not in to_create_ath:
                to_create_ath.append(ath)
            if eve not in to_create_eve:
                to_create_eve.append(eve)
            if ati not in to_create_ati:
                to_create_ati.append(ati)

            # athlete_info.event.add(event)

        Athlete.objects.bulk_create(to_create_ath, batch_size=10000)
        Event.objects.bulk_create(to_create_eve, batch_size=10000)
        AthleteInfo.objects.bulk_create(to_create_ati, batch_size=10000)

        ath_ids = list(AthleteInfo.objects.values_list('id', flat=True))
        eve_ids = Event.objects.values_list('id', flat=True)
        ath_len = len(ath_ids)

        for eve_id in eve_ids:
            link_ath_eve = []
            random.shuffle(ath_ids)

            randon_number = random.randint(0, ath_len)
            link = ath_ids[:randon_number]

            for ath_id in ath_ids:
                link = AthleteInfo.event.through(athleteinfo_id=ath_id, event_id=eve_id)
                link_ath_eve.append(link)

            AthleteInfo.event.through.objects.bulk_create(link_ath_eve, batch_size=10000)

        print("Process completed successfully")