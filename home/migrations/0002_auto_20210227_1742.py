# Generated by Django 3.1.7 on 2021-02-27 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='live_feed',
            old_name='end_time',
            new_name='time_stamp',
        ),
        migrations.RemoveField(
            model_name='live_feed',
            name='start_time',
        ),
    ]
