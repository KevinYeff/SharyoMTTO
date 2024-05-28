# Generated by Django 4.2 on 2024-05-23 22:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact_book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'ciudades',
                'db_table': 'ciudad',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'paises',
                'db_table': 'pais',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=20, unique=True)),
                ('birthday', models.DateField()),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('created_date', models.DateField(default=datetime.datetime(2024, 5, 23, 22, 37, 35, 1609, tzinfo=datetime.timezone.utc))),
                ('update_date', models.DateField(default=datetime.datetime(2024, 5, 23, 22, 37, 35, 1609, tzinfo=datetime.timezone.utc))),
                ('last_login', models.DateField(default=datetime.datetime(2024, 5, 23, 22, 37, 35, 1609, tzinfo=datetime.timezone.utc))),
                ('status', models.BooleanField(default=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.city')),
                ('contact_book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contact_book.contact_book')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuario',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50)),
                ('id_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.country')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'estados',
                'db_table': 'estado',
            },
        ),
    ]