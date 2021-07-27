from django.core import validators
from django import forms
from django.forms import widgets
from .models import Sells
import datetime

class Select(forms.Form):
    agents = (('avesh','Avesh'),('ajay','Ajay'),('','Both'))
    agent_name = forms.ChoiceField(choices = agents, widget = forms.RadioSelect)
    
class SellsForm(forms.ModelForm):
    items = (
        ('sim','SIM'),
        ('recharge','Recharge'),
        ('adhar_widrawal','Adhar Widrawal'),
        ('earphone','Ear-Phone'),
        ('money_transfer','Money Transfer'),
        ('neckband','Neckband'),
        ('charger','Charger'),
        ('otg', 'OTG'),
        ('datacable', 'Data Cable'),
    )
    #agent_name.widget.attrs['class'] = 'form-control'
    item_name = forms.ChoiceField(choices = items, widget = forms.RadioSelect)
    #item_name.widget.attrs['class'] = 'form-control'
    price = forms.IntegerField()
    price.widget.attrs['class'] = 'form-control'
    #ip = 
    class Meta:
        model = Sells
        fields = ['item_name','price','comment','ip']
        widgets = {
            'item_name' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.TextInput(attrs={'class':'form-control'}),
            'comment' : forms.TextInput(attrs={'class':'form-control'}),
            'ip' : forms.HiddenInput()
        }