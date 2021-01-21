from django.db import models
from django.contrib import admin

class Athlete(models.Model):
    id = models.AutoField(
        db_column='athId',
        primary_key=True,
    )
    athlete_name = models.CharField(
        db_column='athName', 
        max_length=45,
        unique = True
    )
    events = models.ManyToManyField(
        'Event',
        db_column='athEvents', 
    )

    def __str__(self):
        return f"{self.id} - {self.athlete_name}"

    class Meta:
        managed = True
        db_table = 'Athlete'

        
admin.site.register(Athlete)