# Generated by Django 4.2 on 2024-06-12 19:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_rename_liters_amount_consumption_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 6, 12, 19, 12, 0, 216302, tzinfo=datetime.timezone.utc)),
        ),
    ]