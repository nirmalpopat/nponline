from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import datetime

class Sells(models.Model):
    item_name = models.CharField(max_length=50)
    price = models.IntegerField()
    comment = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=50,default='')
    date = models.DateField(default=datetime.date.today())
    time = models.TimeField(default=datetime.datetime.now().time())
    
    def __str__(self):
        return self.item_name
    
class Stock(models.Model):
    items = (
        ('earphone','Ear-Phone'),
        ('neckband','Neckband'),
        ('charger','Charger'),
        ('otg', 'OTG'),
        ('datacable', 'Data Cable'),
    )
    item_name = models.CharField(choices = items, max_length=50)
    item_qty = models.IntegerField()
    date = models.DateField(default=datetime.date.today())
    time = models.TimeField(default=datetime.datetime.now().time())
    def __str__(self):
        return self.item_name