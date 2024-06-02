# Generated by Django 4.2 on 2024-05-29 03:48

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
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=20, verbose_name='Apellido')),
                ('mobile', models.CharField(max_length=20, unique=True, verbose_name='Celular')),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=20, unique=True, verbose_name='Correo electronico')),
                ('birth_date', models.DateField(default=datetime.datetime(2024, 5, 29, 3, 48, 46, 2953, tzinfo=datetime.timezone.utc))),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='Nombre de usuario')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('hide_email', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=datetime.datetime(2024, 5, 29, 3, 48, 46, 2953, tzinfo=datetime.timezone.utc))),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.city')),
                ('contact_book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contact_book.contact_book')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.country')),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.state')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuario',
            },
        ),
    ]