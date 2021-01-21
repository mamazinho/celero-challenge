from django.db import models
from django.contrib import admin

class EventInfo(models.Model):
    id = models.AutoField(
        db_column='eviId',
        primary_key=True,
    )
    event = models.ForeignKey(
        'Event',
        db_column='eviEveId',
        default=0,
        on_delete=models.CASCADE
    )
    city = models.CharField(
        db_column='eviCity',
        max_length=45,
        default='',
    )
    sport = models.CharField(
        db_column='eviSport',
        max_length=45,
        default='',
    )
    season = models.CharField(
        db_column='eviSeason',
        max_length=10,
        default='',
    )
    year = models.CharField(
        db_column='eviYear',
        max_length=45,
        default='',
    )
    games = models.CharField(
        db_column='eviGames',
        max_length=45,
        default='',
    )


    def __str__(self):
        return f"{self.id} - {self.event} - {self.city} - {self.sport} - {self.season} - {self.year}"

    class Meta:
        managed = True
        db_table = 'EventInfo'

        
admin.site.register(EventInfo)