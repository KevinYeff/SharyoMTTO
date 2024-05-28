# Generated by Django 4.2 on 2024-05-23 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('mobil', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'contacts',
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Contact_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Contact_book',
                'verbose_name_plural': 'Contact_books',
                'db_table': 'contact_book',
            },
        ),
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('mobil', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=20)),
            ],
            options={
                'verbose_name': 'Mechanic',
                'verbose_name_plural': 'mechanics',
                'db_table': 'mechanic',
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Specialization',
                'verbose_name_plural': 'specializations',
                'db_table': 'specialization',
            },
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('mobil', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Workshop',
                'verbose_name_plural': 'workshops',
                'db_table': 'workshop',
            },
        ),
    ]