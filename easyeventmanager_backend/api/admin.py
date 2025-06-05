from django.contrib import admin
from .models import Event


# PUBLIC_INTERFACE
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Admin panel config for Event."""
    list_display = ('name', 'date', 'time')
    search_fields = ('name',)
    list_filter = ('date',)
