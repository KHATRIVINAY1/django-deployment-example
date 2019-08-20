# Generated by Django 2.2.4 on 2019-08-16 08:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2019, 8, 16, 8, 33, 46, 211878, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]