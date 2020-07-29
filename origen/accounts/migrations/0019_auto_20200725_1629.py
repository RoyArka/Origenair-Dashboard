# Generated by Django 3.0.6 on 2020-07-25 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0040_auto_20200725_1629'),
        ('accounts', '0018_auto_20200724_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='persons', to='organization.Organization'),
        ),
    ]
