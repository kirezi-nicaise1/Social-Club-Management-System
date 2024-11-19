from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm



def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/events_list.html', {'events': events})


@login_required(login_url='/authentication/login')
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()  
    return render(request, 'events/event_form.html', {'form': form})

@login_required(login_url='/authentication/login')
def event_update(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

@login_required
def event_delete(request, pk):
    event = Event.objects.get(pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})

def view_attendees(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    attendees = event.attendees.all()  # Assuming the ManyToManyField is named 'attendees'
    return render(request, 'events/attendees.html', {'event': event, 'attendees': attendees})