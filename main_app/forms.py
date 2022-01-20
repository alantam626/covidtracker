<<<<<<< HEAD
from django.forms import ModelForm, Select
from django import forms
=======
from django.forms import ModelForm
>>>>>>> main
from django.contrib.auth.forms import UserCreationForm
from .models import Kit, Strategy, CustomUser

class KitForm(ModelForm):
    class Meta: 
        model = Kit
        fields = ['date', 'strategy']
        widgets = {
            'name': Select(),
        }

class StrategyForm(ModelForm):
    class Meta:
        model = Strategy
        fields = '__all__'

class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username']

class StateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['state']