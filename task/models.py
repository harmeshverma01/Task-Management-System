from enumchoicefield import  EnumChoiceField
from django.db import models

from user.models import User
from .enum import Category

# Create your models here.

class Task(models.Model):
    CHOICES = (
        ("Todo" , "Todo"),
        ("In_progress", "In_progress"),
        ('completed', 'completed'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee')
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Manager",  null=True)
    title = models.CharField(max_length=50)
    descriptions = models.TextField()
    comment = models.CharField(max_length=200)
    status = models.CharField(choices=CHOICES, max_length=20, default='Todo')
    feedback = models.CharField(max_length=150)
    rating = models.DecimalField(max_digits=5, decimal_places=0)
    
    def __str__(self) -> str:
        return self.title
    