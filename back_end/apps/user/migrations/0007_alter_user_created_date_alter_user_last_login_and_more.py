# Generated by Django 4.2 on 2024-05-27 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rename_birthday_user_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2024, 5, 27, 16, 41, 37, 514688, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateField(default=datetime.datetime(2024, 5, 27, 16, 41, 37, 514688, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='update_date',
            field=models.DateField(default=datetime.datetime(2024, 5, 27, 16, 41, 37, 514688, tzinfo=datetime.timezone.utc)),
        ),
    ]
