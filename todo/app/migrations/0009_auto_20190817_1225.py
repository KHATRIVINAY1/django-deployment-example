# Generated by Django 2.2.4 on 2019-08-17 06:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20190817_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2019, 8, 17, 6, 55, 26, 138655, tzinfo=utc)),
        ),
    ]
