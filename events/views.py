from django.shortcuts import render, get_object_or_404
from events.models import Event


def event(request, event_id):
    """
    A view that shows a singular event
    """
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'event': event
    }

    return render(request, 'events/event.html', context)


def events_list(request, event_type_arg):
    """
    A view that shows all events ordered by type
    """
    if event_type_arg == 'all':
        events = Event.objects.all()
        event_type = 'All Events'
    else:
        events = Event.objects.all()

    context = {
        'events': events,
        'event_type': event_type
    }

    return render(request, 'events/events-list.html', context)


def add_event(request):
    return render(request, 'events/add-event.html')


def edit_event(request):
    return render(request, 'events/edit-event.html')
