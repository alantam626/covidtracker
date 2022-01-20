from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# from re import S


# Create your models here.
class CustomUser(AbstractUser):
    country = models.CharField(max_length=30, blank=True)

class Strategy(models.Model):
    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    
class Kit(models.Model):
    date = models.DateField()
    strategy = models.ManyToManyField(Strategy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('kit_detail', kwargs={'pk': self.id})
        
class State(models.Model):
    name = models.CharField(max_length = 30)
    confirmed = models.IntegerField()
    death = models.IntegerField()
    lat = models.CharField(max_length = 10)
    long = models.CharField(max_length = 10)