# Generated by Django 4.2 on 2024-06-14 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_order', '0006_alter_work_order_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_order',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 14, 15, 59, 53, 384465, tzinfo=datetime.timezone.utc)),
        ),
    ]
