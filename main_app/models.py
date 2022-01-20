from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    state = models.CharField(max_length=30, blank=True)

class Strategy(models.Model):
    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    
class Kit(models.Model):
    date = models.DateField()
    strategy = models.ManyToManyField(Strategy)
    
    def get_absolute_url(self):
        return reverse('kit_detail', kwargs={'pk': self.id})
        
class State(models.Model):
    name = models.CharField(max_length = 30)
    confirmed = models.IntegerField()
    death = models.IntegerField()
    lat = models.CharField(max_length = 10)
    long = models.CharField(max_length = 10)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    vaccine_card = models.ForeignKey(Strategy, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for strategy_id: {self.strategy_id} @{self.url}"