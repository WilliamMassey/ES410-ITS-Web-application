# Generated by Django 3.1.4 on 2021-01-28 14:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField(default=datetime.datetime(2020, 12, 31, 12, 0))),
                ('end_datetime', models.DateTimeField(default=datetime.datetime(2020, 12, 31, 13, 0))),
            ],
        ),
        migrations.CreateModel(
            name='Booking_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_slots', models.JSONField(default={'00:00:00': 0, '00:15:00': 0, '00:30:00': 0, '00:45:00': 0, '01:00:00': 0, '01:15:00': 0, '01:30:00': 0, '01:45:00': 0, '02:00:00': 0, '02:15:00': 0, '02:30:00': 0, '02:45:00': 0, '03:00:00': 0, '03:15:00': 0, '03:30:00': 0, '03:45:00': 0, '04:00:00': 0, '04:15:00': 0, '04:30:00': 0, '04:45:00': 0, '05:00:00': 0, '05:15:00': 0, '05:30:00': 0, '05:45:00': 0, '06:00:00': 0, '06:15:00': 0, '06:30:00': 0, '06:45:00': 0, '07:00:00': 0, '07:15:00': 0, '07:30:00': 0, '07:45:00': 0, '08:00:00': 0, '08:15:00': 0, '08:30:00': 0, '08:45:00': 0, '09:00:00': 0, '09:15:00': 0, '09:30:00': 0, '09:45:00': 0, '10:00:00': 0, '10:15:00': 0, '10:30:00': 0, '10:45:00': 0, '11:00:00': 0, '11:15:00': 0, '11:30:00': 0, '11:45:00': 0, '12:00:00': 0, '12:15:00': 0, '12:30:00': 0, '12:45:00': 0, '13:00:00': 0, '13:15:00': 0, '13:30:00': 0, '13:45:00': 0, '14:00:00': 0, '14:15:00': 0, '14:30:00': 0, '14:45:00': 0, '15:00:00': 0, '15:15:00': 0, '15:30:00': 0, '15:45:00': 0, '16:00:00': 0, '16:15:00': 0, '16:30:00': 0, '16:45:00': 0, '17:00:00': 0, '17:15:00': 0, '17:30:00': 0, '17:45:00': 0, '18:00:00': 0, '18:15:00': 0, '18:30:00': 0, '18:45:00': 0, '19:00:00': 0, '19:15:00': 0, '19:30:00': 0, '19:45:00': 0, '20:00:00': 0, '20:15:00': 0, '20:30:00': 0, '20:45:00': 0, '21:00:00': 0, '21:15:00': 0, '21:30:00': 0, '21:45:00': 0, '22:00:00': 0, '22:15:00': 0, '22:30:00': 0, '22:45:00': 0, '23:00:00': 0, '23:15:00': 0, '23:30:00': 0, '23:45:00': 0})),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_number_plate', models.CharField(default=None, max_length=8, primary_key=True, serialize=False)),
                ('colour', models.CharField(choices=[('b', 'BLUE'), ('r', 'RED'), ('g', 'GREEN'), ('y', 'YELLOW'), ('o', 'ORANGE'), ('s', 'BLACK'), ('n', 'BROWN'), ('w', 'WHITE')], default='s', max_length=1)),
                ('manufacturer', models.CharField(default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User_Car_Mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.car')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_parking', models.BooleanField(default=False)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]