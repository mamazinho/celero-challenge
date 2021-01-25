from django.db import models
from django.contrib import admin

class AthleteInfo(models.Model):
    id = models.AutoField(
        db_column='atiId',
        primary_key=True,
    )
    athlete = models.ForeignKey(
        'Athlete',
        db_column='atiAthId',
        default=0,
        on_delete=models.CASCADE,
        related_name='athlete_infos'
    )
    event = models.ManyToManyField(
        'Event',
        db_column='atiEveId',
        default=0,
        related_name='athlete_infos',
        blank=True
    )
    sex = models.CharField(
        db_column='atiSex',
        max_length=1,
        choices=[(x, x) for x in ('F', 'M')],
        default='F',
    )
    age = models.PositiveSmallIntegerField(
        db_column='atiAge',
        null=True,
        blank=True,
    )
    height = models.FloatField(
        db_column='atiHeight',
        null=True,
        blank=True,
    )
    weight = models.FloatField(
        db_column='atiWeight',
        null=True,
        blank=True,
    )
    team = models.CharField(
        db_column='atiTeam',
        max_length=65,
        default=0,
    )
    medal = models.CharField(
        db_column='atiMedal',
        max_length=6,
        choices=[(x, x) for x in ('Silver', 'Gold', 'Bronze')],
        null=True,
        blank=True,
    )


    def __str__(self):
        return f"{self.id} - {self.athlete} - {self.sex} - {self.age} - {self.team} - {self.medal}"

    class Meta:
        managed = True
        db_table = 'AthleteInfo'
        unique_together = ['athlete', 'sex', 'team', 'age', 'height', 'weight', 'medal']

        
admin.site.register(AthleteInfo)