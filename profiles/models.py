from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    A model for users
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns the username
        """
        return self.user.username
