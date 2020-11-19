from django.db import models
# default django user model imports
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager 
# Create your models here.

class UserProfileManager(BaseUserManager):
    """ manager for user profiles"""
    def create_user(self, email, name, password=None):
        """ Create a new user profile"""
        if not email:
            raise ValueError("users must have email address")
        
        # normalize the email address meaning making 2nd half lowercase
        email = self.normalize_email(email)
        user =  self.model(email=email, name=name)
        # sets encrypted password
        user.set_password(password)
        # standard syntax for db
        user.save(using=self._db)
        return user
    
    def create_super_user(self, email, name, password):
        """ create super user"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
        
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Db model for users in app
    """
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    # custom model manager for user to control users django knows how to work with userprofile model
    objects = UserProfileManager()
    # override default user name with email field for authenticating with email
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]
    
    def get_full_name(self):
        """ retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """ retrieve short name of user """
        return self.name
    
    def __str__(self):
        """ return string representation of user (Recommended for django models to convert object to string)"""
        return self.email 