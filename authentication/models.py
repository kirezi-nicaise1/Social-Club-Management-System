from django.db import models
from django.contrib.auth.models import AbstractUser

class Admin(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('User', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='User')
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "admin"