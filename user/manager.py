
from django.contrib.auth.models import  BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email,  password=None):
        if not email:
            raise ValueError("User must have email address")
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password),
        user.save(using=self._db)
        return user
    
    def staff_user(self, email, password):
        user = self.create_user(
            email,
            password=password
        )
        user.is_staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        print(user.__dict__)
        return user
    
    