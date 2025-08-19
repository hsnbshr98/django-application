from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Event
from .forms import EventForm
from django.utils.timezone import now
from datetime import datetime, timedelta

def event_list(request):
    query = request.GET.get('q')
    status_filter = request.GET.get('status')
    date_filter = request.GET.get('date')
    
    events = Event.objects.all()
    
    if query:
        events = events.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query)
        )
    
    if status_filter:
        events = events.filter(status=status_filter)
    
    if date_filter:
        if date_filter == 'today':
            start_date = now().date()
            end_date = start_date + timedelta(days=1)
        elif date_filter == 'week':
            start_date = now().date()
            end_date = start_date + timedelta(days=7)
        elif date_filter == 'month':
            start_date = now().date()
            end_date = start_date + timedelta(days=30)
        else:
            start_date = None
            end_date = None
        
        if start_date and end_date:
            events = events.filter(date_time__date__range=[start_date, end_date])
    
    return render(request, 'events/event_list.html', {
        'events': events,
        'status_choices': Event.STATUS_CHOICES
    })

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    
    return render(request, 'events/event_form.html', {'form': form, 'title': 'Create Event'})

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    
    return render(request, 'events/event_form.html', {'form': form, 'title': 'Edit Event'})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    
    return render(request, 'events/event_confirm_delete.html', {'event': event})