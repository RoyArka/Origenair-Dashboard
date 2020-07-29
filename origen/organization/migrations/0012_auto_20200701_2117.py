# Generated by Django 3.0.6 on 2020-07-02 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0011_auto_20200701_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='email',
            field=models.CharField(blank=True, default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='organization',
            name='website',
            field=models.CharField(blank=True, default='None', max_length=200, null=True),
        ),
    ]
