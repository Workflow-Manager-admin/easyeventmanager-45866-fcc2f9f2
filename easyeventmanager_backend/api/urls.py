from django.urls import path
from .views import health, event_list_create, event_detail

urlpatterns = [
    path('health/', health, name='Health'),
    path('events/', event_list_create, name='event-list-create'),
    path('events/<int:event_id>/', event_detail, name='event-detail'),
]
