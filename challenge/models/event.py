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

    def __str__(self):
        return f"{self.id} - {self.event_name}"

    class Meta:
        managed = True
        db_table = 'Event'

        
admin.site.register(Event)