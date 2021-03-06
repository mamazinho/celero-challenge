# Generated by Django 3.1.5 on 2021-01-21 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(db_column='athId', primary_key=True, serialize=False)),
                ('athlete_name', models.CharField(db_column='athName', max_length=45, unique=True)),
            ],
            options={
                'db_table': 'Athlete',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(db_column='eveId', primary_key=True, serialize=False)),
                ('event_name', models.CharField(db_column='eveName', max_length=132, unique=True)),
            ],
            options={
                'db_table': 'Event',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EventInfo',
            fields=[
                ('id', models.AutoField(db_column='eviId', primary_key=True, serialize=False)),
                ('city', models.CharField(db_column='eviCity', default='', max_length=45)),
                ('sport', models.CharField(db_column='eviSport', default='', max_length=45)),
                ('season', models.CharField(db_column='eviSeason', default='', max_length=10)),
                ('year', models.CharField(db_column='eviYear', default='', max_length=45)),
                ('games', models.CharField(db_column='eviGames', default='', max_length=45)),
                ('event', models.ForeignKey(db_column='eviEveId', default=0, on_delete=django.db.models.deletion.CASCADE, to='challenge.event')),
            ],
            options={
                'db_table': 'EventInfo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AthleteInfo',
            fields=[
                ('id', models.AutoField(db_column='atiId', primary_key=True, serialize=False)),
                ('sex', models.CharField(choices=[('F', 'F'), ('M', 'M')], db_column='atiSex', default='F', max_length=1)),
                ('age', models.IntegerField(blank=True, db_column='atiAge', null=True)),
                ('height', models.FloatField(blank=True, db_column='atiHeight', null=True)),
                ('weight', models.FloatField(blank=True, db_column='atiWeight', null=True)),
                ('team', models.CharField(db_column='atiTeam', default=0, max_length=65)),
                ('medal', models.CharField(blank=True, choices=[('Silver', 'Silver'), ('Gold', 'Gold'), ('Bronze', 'Bronze')], db_column='atiMedal', max_length=6, null=True)),
                ('athlete', models.ForeignKey(db_column='atiAthId', default=0, on_delete=django.db.models.deletion.CASCADE, to='challenge.athlete')),
            ],
            options={
                'db_table': 'AthleteInfo',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='athlete',
            name='events',
            field=models.ManyToManyField(db_column='athEvents', to='challenge.Event'),
        ),
    ]
