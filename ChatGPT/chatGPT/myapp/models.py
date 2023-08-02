from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Chat(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    message = models.TextField(default="")
    response = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}:{self.message}'