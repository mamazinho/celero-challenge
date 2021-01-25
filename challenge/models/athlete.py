from django.db import models
from django.contrib import admin

class Athlete(models.Model):
    id = models.AutoField(
        db_column='athId',
        primary_key=True,
    )
    athlete_name = models.CharField(
        db_column='athName', 
        max_length=255,
        default='',
        unique = True
    )

    def __str__(self):
        return f"{self.id} - {self.athlete_name}"

    class Meta:
        managed = True
        db_table = 'Athlete'

    @property
    def athlete_name_sliced(self):
        return self.athlete_name[:24]

        
admin.site.register(Athlete)