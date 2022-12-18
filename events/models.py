from django.db import models


class Event(models.Model):
    """
    Defines attributes of the event model
    """
    title = models.CharField(max_length=254)
    description = models.TextField()
    category = models.CharField(max_length=254, null=True)
    location = models.CharField(max_length=254, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.CharField(max_length=24, null=True)
    people = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.CharField(max_length=254, null=True, blank=True)
    online = models.BooleanField(default=False)

    def __str__(self):
        return self.title
