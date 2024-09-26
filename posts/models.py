from django.db import models


class Post(models.Model):
    """Post model"""

    text = models.TextField()

    def __str__(self):
        """String method"""
        return str(self.text)[:50]
