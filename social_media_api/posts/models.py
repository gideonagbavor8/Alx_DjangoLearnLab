from django.db import models
from accounts.models import CustomUser

class Post(models.Model):
    author = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='authored_posts'  # Use a unique related_name
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name='post_comments'  # Unique related_name for comments on a post
    )
    author = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='authored_comments'  # Unique related_name for comments by a user
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
