# Generated by Django 2.1.3 on 2018-11-12 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_program_radio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='radio',
            field=models.IntegerField(choices=[(1, 'Radio Globo'), (2, 'CBN'), (3, 'BH')], default=1),
        ),
    ]
