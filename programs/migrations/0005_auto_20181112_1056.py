# Generated by Django 2.1.3 on 2018-11-12 10:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0004_auto_20181112_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='end date time'),
        ),
        migrations.AlterField(
            model_name='program',
            name='start',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='start date time'),
        ),
    ]
