from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_time', 'location', 'status', 'created_at')
    list_filter = ('status', 'date_time')
    search_fields = ('title', 'location', 'description')
    date_hierarchy = 'date_time'