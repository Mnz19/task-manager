from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_document = models.CharField(max_length=11, unique=True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['username']
        
