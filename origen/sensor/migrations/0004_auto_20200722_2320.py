# Generated by Django 3.0.6 on 2020-07-23 06:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0003_auto_20200722_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
