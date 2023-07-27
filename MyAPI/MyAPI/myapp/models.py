from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=500)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.name