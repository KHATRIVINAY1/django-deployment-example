# Generated by Django 2.2.4 on 2019-08-18 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20190818_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 18, 13, 29, 59, 808751)),
        ),
    ]
