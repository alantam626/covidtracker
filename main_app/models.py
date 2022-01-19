from django.db import models
from django.urls import reverse
# from re import S


# Create your models here.

class Strategy(models.Model):
    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    
class Kit(models.Model):
    date = models.DateField()
    strategy = models.ManyToManyField(Strategy)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kit_detail', kwargs={'pk': self.id})
        
class State(models.Model):
    confirmed = models.IntegerField()
    death = models.IntegerField()
    lat = models.CharField(max_length = 10)
    long = models.CharField(max_length = 10)