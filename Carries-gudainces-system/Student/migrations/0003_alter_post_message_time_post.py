# Generated by Django 4.0.1 on 2022-01-24 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_remove_ugr_usr_leader_remove_ugroup_learder_priority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_message',
            name='time_post',
            field=models.CharField(default=datetime.datetime(2022, 1, 24, 3, 5, 46, 43939), max_length=255),
        ),
    ]