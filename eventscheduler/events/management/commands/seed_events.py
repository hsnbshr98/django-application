# events/management/commands/seed_events.py
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from datetime import datetime, timedelta
from events.models import Event
import random

class Command(BaseCommand):
    help = 'Seeds the database with sample events'

    def handle(self, *args, **options):
        # Clear existing events
        Event.objects.all().delete()
        
        # Sample events data
        events_data = [
            {
                'title': 'Team Meeting',
                'description': 'Weekly team sync to discuss project progress and blockers',
                'date_time': make_aware(datetime.now() + timedelta(hours=2)),
                'location': 'Conference Room A',
                'status': 'attending'
            },
            {
                'title': 'Product Launch',
                'description': 'Launch of our new product line with demo and Q&A session',
                'date_time': make_aware(datetime.now() + timedelta(days=5)),
                'location': 'Main Auditorium',
                'status': 'upcoming'
            },
            {
                'title': 'Client Presentation',
                'description': 'Presenting quarterly results to our key client stakeholders',
                'date_time': make_aware(datetime.now() + timedelta(days=2, hours=3)),
                'location': 'Client Office - Downtown',
                'status': 'maybe'
            },
            {
                'title': 'Code Review',
                'description': 'Review of the new authentication system implementation',
                'date_time': make_aware(datetime.now() + timedelta(days=1, hours=1)),
                'location': 'Dev Room B',
                'status': 'attending'
            },
            {
                'title': 'Company Retreat',
                'description': 'Annual company retreat for team building and strategy planning',
                'date_time': make_aware(datetime.now() + timedelta(days=14)),
                'location': 'Mountain Lodge Resort',
                'status': 'upcoming'
            },
            {
                'title': 'Training Workshop',
                'description': 'Advanced Django training workshop for the development team',
                'date_time': make_aware(datetime.now() + timedelta(days=3)),
                'location': 'Training Room C',
                'status': 'attending'
            },
            {
                'title': 'Budget Meeting',
                'description': 'Quarterly budget review and planning for next quarter',
                'date_time': make_aware(datetime.now() + timedelta(days=7)),
                'location': 'Finance Department',
                'status': 'declined'
            },
            {
                'title': 'Networking Event',
                'description': 'Industry networking event with potential partners and clients',
                'date_time': make_aware(datetime.now() + timedelta(days=10)),
                'location': 'Convention Center',
                'status': 'maybe'
            },
            {
                'title': 'Product Demo',
                'description': 'Live demo of new features for the sales team',
                'date_time': make_aware(datetime.now() + timedelta(days=4, hours=2)),
                'location': 'Demo Room',
                'status': 'attending'
            },
            {
                'title': 'HR Training',
                'description': 'Mandatory HR training on workplace policies and procedures',
                'date_time': make_aware(datetime.now() + timedelta(days=6)),
                'location': 'HR Conference Room',
                'status': 'declined'
            }
        ]

        # Create events
        for event_data in events_data:
            Event.objects.create(**event_data)
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully seeded {len(events_data)} events')
        )