# Generated by Django 3.0.6 on 2020-06-22 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200621_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='job_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
