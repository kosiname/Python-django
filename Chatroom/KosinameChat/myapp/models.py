from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    roomname = models.CharField(max_length=5000)
    

class Message(models.Model):
    value = models.CharField(max_length=6000000, default="")
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000, default="")
    room = models.CharField(max_length=5000, default="")
