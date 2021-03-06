from django.db import models
from django.contrib import admin

class Event(models.Model):
    id = models.AutoField(
        db_column='eveId',
        primary_key=True,
    )
    event_name = models.CharField(
        db_column='eveName', 
        max_length=132,
    )
    city = models.CharField(
        db_column='eveCity',
        max_length=45,
        default='',
    )
    sport = models.CharField(
        db_column='eveSport',
        max_length=64,
        default='',
    )
    season = models.CharField(
        db_column='eveSeason',
        max_length=10,
        default='',
    )
    year = models.PositiveSmallIntegerField(
        db_column='eveYear',
        default=0,
    )
    games = models.CharField(
        db_column='eveGames',
        max_length=70,
        default='',
    )

    def __str__(self):
        return f"{self.id} - {self.event_name} - {self.city} - {self.sport} - {self.season} - {self.year}"

    class Meta:
        managed = True
        db_table = 'Event'
        unique_together = ['event_name', 'city', 'sport', 'season', 'year', 'games']

        
admin.site.register(Event)