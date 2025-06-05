from django.db import models


# PUBLIC_INTERFACE
class Event(models.Model):
    """Model representing an event with its details."""

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} ({self.date} {self.time})"
