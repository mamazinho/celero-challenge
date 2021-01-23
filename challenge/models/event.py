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
        unique = True
    )
    city = models.CharField(
        db_column='eveCity',
        max_length=45,
        default='',
    )
    sport = models.CharField(
        db_column='eveSport',
        max_length=45,
        default='',
    )
    season = models.CharField(
        db_column='eveSeason',
        max_length=10,
        default='',
    )
    year = models.CharField(
        db_column='eveYear',
        max_length=45,
        default='',
    )

    def __str__(self):
        return f"{self.id} - {self.event_name} - {self.city} - {self.sport} - {self.season} - {self.year}"

    class Meta:
        managed = True
        db_table = 'Event'

        
admin.site.register(Event)