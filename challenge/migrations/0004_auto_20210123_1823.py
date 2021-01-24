# Generated by Django 3.1.5 on 2021-01-23 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0003_auto_20210123_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='games',
            field=models.CharField(db_column='eveGames', default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='athleteinfo',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, db_column='atiAge', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='sport',
            field=models.CharField(db_column='eveSport', default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='event',
            name='year',
            field=models.PositiveSmallIntegerField(db_column='eveYear', default=0),
        ),
    ]
