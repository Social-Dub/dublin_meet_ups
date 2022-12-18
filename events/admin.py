from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    """
    Defines the field order in the admin
    """
    model = Event
    fields = (
        'title', 'description', 'date', 'category', 'location', 'user',
        'people', 'image', 'image_url')


admin.site.register(Event)
