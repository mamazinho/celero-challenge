# Generated by Django 3.1.5 on 2021-01-24 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0008_auto_20210124_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='athlete_name',
        ),
    ]
