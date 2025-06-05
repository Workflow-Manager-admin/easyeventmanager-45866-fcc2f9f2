from rest_framework import serializers
from .models import Event


# PUBLIC_INTERFACE
class EventSerializer(serializers.ModelSerializer):
    """Serializes Event model for API request/response."""

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'date', 'time']
