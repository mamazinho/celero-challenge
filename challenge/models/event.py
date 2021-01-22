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
    athlete_infos = models.ManyToManyField(
        'AthleteInfo',
        db_column='eveAtiId', 
        related_name='events'
    )

    def __str__(self):
        return f"{self.id} - {self.event_name} - {self.athlete_infos}"

    class Meta:
        managed = True
        db_table = 'Event'

        
admin.site.register(Event)