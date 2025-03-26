from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    # Users following this user
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='user_following',
        blank=True
    )

    # Users this user is following
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='user_followers',
        blank=True
    )

    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # Unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
