from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("User must have email address")

        email= self.noramalize_email(email)
        user= self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """Create a super user"""
        user.create_user(email,name, password)
        self.is_superuser=True
        self.is_staff=True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)

    objects =UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELD=['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def _str_(self):
        return self.email
