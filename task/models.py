
from email.policy import default
from django.db import models

from user.models import User



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
    completed_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    status = models.CharField(choices=CHOICES, max_length=20, default='Todo')
    feedback = models.CharField(max_length=150)
    rating = models.DecimalField(max_digits=5, decimal_places=0)
    amount_per_hour = models.FloatField()
    working_hours = models.FloatField()
    
    def __str__(self) -> str:
        return self.title
    