# Generated by Django 4.2 on 2024-05-27 01:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0008_alter_consumption_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 5, 27, 1, 42, 32, 888444, tzinfo=datetime.timezone.utc)),
        ),
    ]
