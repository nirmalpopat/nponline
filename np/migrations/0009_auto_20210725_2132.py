# Generated by Django 3.2.4 on 2021-07-25 16:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('np', '0008_auto_20210725_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='sells',
            name='ip',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='sells',
            name='time',
            field=models.TimeField(default=datetime.time(21, 32, 33, 247430)),
        ),
        migrations.AlterField(
            model_name='stock',
            name='time',
            field=models.TimeField(default=datetime.time(21, 32, 33, 247430)),
        ),
    ]
