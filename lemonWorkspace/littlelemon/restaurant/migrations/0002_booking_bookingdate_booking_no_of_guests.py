# Generated by Django 5.0.3 on 2024-03-23 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='bookingDate',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
