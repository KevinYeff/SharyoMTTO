# Generated by Django 4.2 on 2024-06-10 17:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=250)),
            ],
            options={
                'verbose_name': 'Vehicle_category',
                'verbose_name_plural': 'vehicle_categories',
                'db_table': 'vehicle_category',
            },
        ),
        migrations.CreateModel(
            name='Vehicle_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=250)),
            ],
            options={
                'verbose_name': 'Vehicle_type',
                'verbose_name_plural': 'vehicle_types',
                'db_table': 'vehicle_type',
            },
        ),
        migrations.CreateModel(
            name='Vehicle_brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.country')),
                ('vehicle_categories', models.ManyToManyField(to='vehicles.vehicle_category')),
                ('vehicle_types', models.ManyToManyField(to='vehicles.vehicle_type')),
            ],
            options={
                'verbose_name': 'Vehicle_brand',
                'verbose_name_plural': 'vehicle_brands',
                'db_table': 'vehicle_brand',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=10, unique=True)),
                ('model', models.IntegerField(blank=True, max_length=4, null=True)),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('fuel_type', models.CharField(choices=[('ELECTRICO', 'ELECTRICO'), ('EXTRA', 'EXTRA'), ('DIESEL', 'DIESEL'), ('GASOLINA', 'GASOLINA'), ('GAS', 'GAS')], default='GASOLINA', max_length=15)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.vehicle_brand')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('vehicle_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.vehicle_category')),
                ('vehicle_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.vehicle_type')),
            ],
            options={
                'verbose_name': 'Vehicle',
                'verbose_name_plural': 'vehicles',
                'db_table': 'vehicle',
            },
        ),
        migrations.CreateModel(
            name='Mileage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.IntegerField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
            options={
                'verbose_name': 'Mileage',
                'verbose_name_plural': 'mileage',
                'db_table': 'mileage',
            },
        ),
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('km_traveled', models.FloatField()),
                ('amount', models.FloatField()),
                ('price', models.FloatField()),
                ('date', models.DateField(default=datetime.datetime(2024, 6, 10, 17, 2, 18, 956267, tzinfo=datetime.timezone.utc))),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
            options={
                'verbose_name': 'Consumption',
                'verbose_name_plural': 'consumptions',
                'db_table': 'consumption',
            },
        ),
    ]
