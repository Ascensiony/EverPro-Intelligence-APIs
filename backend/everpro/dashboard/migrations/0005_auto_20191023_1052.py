# Generated by Django 2.2.6 on 2019-10-23 10:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20191023_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earnings',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Date'),
        ),
    ]
