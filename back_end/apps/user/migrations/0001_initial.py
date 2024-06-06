# Generated by Django 4.2 on 2024-06-06 03:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=20, verbose_name='Apellido')),
                ('mobile', models.CharField(max_length=20, unique=True, verbose_name='Celular')),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electronico')),
                ('birth_date', models.DateField(default=datetime.datetime(2024, 6, 6, 3, 7, 24, 955646, tzinfo=datetime.timezone.utc))),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='Nombre de usuario')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=datetime.datetime(2024, 6, 6, 3, 7, 24, 955721, tzinfo=datetime.timezone.utc))),
                ('last_login', models.DateTimeField(default=datetime.datetime(2024, 6, 6, 3, 7, 24, 955729, tzinfo=datetime.timezone.utc))),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuario',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('shortname', models.CharField(blank=True, max_length=3)),
                ('phonecode', models.CharField(blank=True, max_length=7)),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'paises',
                'db_table': 'pais',
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
                'verbose_name': 'Estados',
                'verbose_name_plural': 'estados',
                'db_table': 'estados',
            },
        ),
        migrations.CreateModel(
            name='OneTimePassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('id_state', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user.state')),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'ciudades',
                'db_table': 'ciudad',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.city'),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.country'),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.state'),
        ),
    ]
