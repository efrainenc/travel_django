# Generated by Django 4.1.5 on 2023-01-26 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0002_spot_image_alter_location_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='release_date',
        ),
    ]
