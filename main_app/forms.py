from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import ModelForm
from .models import Kit, Strategy

class KitForm(ModelForm):
    class Meta: 
        model = Kit
        fields = ['date', 'strategy']

class StrategyForm(ModelForm):
    class Meta:
        model = Strategy
        fields = '__all__'

