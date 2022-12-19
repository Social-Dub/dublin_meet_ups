from django.shortcuts import render, redirect, reverse, get_object_or_404
from events.models import Event
from events.forms import EventForm
from django.contrib.auth.decorators import login_required


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
        events = Event.objects.filter(category=event_type_arg)
        event_type = event_type_arg
    context = {
        'events': events,
        'event_type': event_type
    }

    return render(request, 'events/events-list.html', context)


@login_required
def add_event(request):
    """
    A view for users to create events
    """
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            user = request.user
            title = request.POST.get('title')
            location = request.POST.get('location')
            people = request.POST.get('people')
            category = request.POST.get('category')
            description = request.POST.get('description')
            event = form.save()
            return redirect(reverse('event', args=[event.id]))
        else:
            print("Form invalid")
            user = request.user
            print('user')
            print(user)
            title = request.POST.get('title')
            print('title')
            print(title)
            location = request.POST.get('location')
            print('location')
            print(location)
            people = request.POST.get('people')
            print('people')
            print(people)
            category = request.POST.get('category')
            print('category')
            print(category)
            description = request.POST.get('description')
            print('description')
            print(description)
            return redirect(reverse('add_event'))

    return render(request, 'events/add-event.html')


def edit_event(request):
    return render(request, 'events/edit-event.html')
