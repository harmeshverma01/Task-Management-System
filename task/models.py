from django.db import models

from user.manager import UserManager
from user.models import User

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    title = models.CharField(max_length=50)
    discriptions = models.TextField()
    completed = models.BooleanField(default=False, blank=True)
    objects = UserManager()
    
    def __str__(self) -> str:
        return self.title