# Generated by Django 3.1.5 on 2021-01-14 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Flights',
            new_name='Flight',
        ),
    ]
