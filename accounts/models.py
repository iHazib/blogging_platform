from django.db import models
from django.contrib.auth.models import AbstractUser

# using abstract user model to create custom user model with additional fields like name, phone number and role.

class CustomUser(AbstractUser):  # abstract base user, permission mixin 
    class Roles(models.TextChoices):   # roles choices, writer or reader
        WRITER = 'writer', 'Writer'
        READER = 'reader', 'Reader'

    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15, blank=True, null=True) # mobile number must be unique for each user.  
    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=Roles.READER,
    )

def __str__(self):
    return f"{self.username} ({self.role})"
