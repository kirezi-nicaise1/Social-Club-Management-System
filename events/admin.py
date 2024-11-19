from django.contrib import admin
from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    filter_horizontal = ('attendees',)  # This makes a nice interface for selecting members

admin.site.register(Event, EventAdmin)

