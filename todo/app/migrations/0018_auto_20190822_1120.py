# Generated by Django 2.2.4 on 2019-08-22 05:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20190822_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 22, 11, 20, 59, 512761)),
        ),
    ]
