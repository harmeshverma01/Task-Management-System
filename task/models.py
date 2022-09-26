from django.db import models

from user.models import User

# Create your models here.

class Task(models.Model):
    CHOICES = (
        ("Todo" , "Todo"),
        ("In_progress", "In_progress"),
        ('completed', 'completed'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee')
    manager = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    descriptions = models.TextField()
    status = models.CharField(choices=CHOICES, max_length=20, default='Todo')
    
    def __str__(self) -> str:
        return self.title
    
class CreateUser(models.Model):
    user1 = models.CharField(max_length=50)
    user2 = models.CharField(max_length=50)    