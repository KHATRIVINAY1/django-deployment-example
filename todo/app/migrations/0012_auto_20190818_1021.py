# Generated by Django 2.2.4 on 2019-08-18 04:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190817_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2019, 8, 18, 4, 51, 30, 637971, tzinfo=utc)),
        ),
    ]
