# Generated by Django 4.2 on 2024-06-13 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_alter_consumption_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 6, 13, 18, 16, 38, 178315, tzinfo=datetime.timezone.utc)),
        ),
    ]