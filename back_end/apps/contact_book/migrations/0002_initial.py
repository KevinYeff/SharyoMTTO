# Generated by Django 4.2 on 2024-05-29 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('contact_book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.city'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.country'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='specialization',
            field=models.ManyToManyField(to='contact_book.specialization'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.state'),
        ),
        migrations.AddField(
            model_name='store',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.city'),
        ),
        migrations.AddField(
            model_name='store',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.country'),
        ),
        migrations.AddField(
            model_name='store',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.state'),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.city'),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.country'),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='specialization',
            field=models.ManyToManyField(to='contact_book.specialization'),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.state'),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact_book.workshop'),
        ),
        migrations.AddField(
            model_name='contact_book',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact_book.contact'),
        ),
        migrations.AddField(
            model_name='contact_book',
            name='mechanic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact_book.mechanic'),
        ),
        migrations.AddField(
            model_name='contact_book',
            name='workshop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact_book.workshop'),
        ),
        migrations.AddField(
            model_name='contact',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.city'),
        ),
        migrations.AddField(
            model_name='contact',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.country'),
        ),
        migrations.AddField(
            model_name='contact',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.state'),
        ),
    ]