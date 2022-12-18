from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('<str:event_type_arg>', views.events_list, name='events_list'),
    path('event/<int:event_id>', views.event, name='event'),
    path('add_event/', views.add_event, name='add_event'),
    path('edit_event/', views.edit_event, name='edit_event'),
]
