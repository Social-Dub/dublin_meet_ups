"""
Contains the forms for the events app.
"""
from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    """
    Generates the form the user will complete to create an event
    """
    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and classes, removes auto-generated labels and sets
        autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Name',
            'description': 'Description',
            'category': 'Category',
            'location': 'Location',
            'date': 'Date/time',
            'people': 'People',
            'online': 'Online',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
