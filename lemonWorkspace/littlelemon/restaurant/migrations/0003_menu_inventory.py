# Generated by Django 5.0.3 on 2024-03-23 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_booking_bookingdate_booking_no_of_guests'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
