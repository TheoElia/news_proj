# Generated by Django 2.2.2 on 2019-06-10 03:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190602_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 10, 3, 24, 13, 656585, tzinfo=utc)),
        ),
    ]
