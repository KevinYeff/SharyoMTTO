# Generated by Django 4.2 on 2024-06-13 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 13, 18, 15, 48, 221659, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 13, 18, 15, 48, 221739, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 13, 18, 15, 48, 221747, tzinfo=datetime.timezone.utc)),
        ),
    ]
