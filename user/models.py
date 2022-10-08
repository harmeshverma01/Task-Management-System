from django.db import models
from django.contrib.auth.models import AbstractBaseUser

import uuid

from .manager import UserManager


class User(AbstractBaseUser):
    ROLE = (
        ("admin", "admin"),
        ("manager", "manager"),
        ("employee", "employee")
    )
    id = models.UUIDField(default=uuid.uuid1, primary_key=True,  unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    role = models.CharField(choices=ROLE, max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=True)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def __str__(self) -> str:
        return self.email
    
    

    