# Generated by Django 3.0.6 on 2020-05-11 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200511_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insightdetails',
            name='season_number',
            field=models.IntegerField(default=1),
        ),
    ]
