from django.db import models

from user.manager import UserManager
from user.models import User

# Create your models here.


class Task(models.Model):
    CHOICES = (
        ("Todo" , "Todo"),
        ("In_progress", "Inprogress"),
        ('completed', 'completed'),
        ('incomplete', 'incomplete')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee')
    title = models.CharField(max_length=50)
    descriptions = models.TextField()
    status = models.CharField(choices=CHOICES, max_length=20, default='Todo')
    # completed = models.BooleanField(default=False, blank=True)
    #status choice field,  Also manager field
    # objects = UserManager()
    
    def __str__(self) -> str:
        return self.title