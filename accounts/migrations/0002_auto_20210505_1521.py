# Generated by Django 3.1.7 on 2021-05-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_datetime',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_datetime',
            field=models.CharField(default='', max_length=30),
        ),
    ]
