# Generated by Django 3.1.8 on 2021-05-04 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210504_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carpark',
            name='geometry',
        ),
    ]
