# Generated by Django 3.2.4 on 2021-07-25 06:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('np', '0006_auto_20210725_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(choices=[('earphone', 'Ear-Phone'), ('neckband', 'Neckband'), ('charger', 'Charger'), ('otg', 'OTG'), ('datacable', 'Data Cable')], max_length=50)),
                ('item_qty', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='sells',
            name='time',
            field=models.TimeField(default=datetime.time(12, 11, 15, 617769)),
        ),
    ]
