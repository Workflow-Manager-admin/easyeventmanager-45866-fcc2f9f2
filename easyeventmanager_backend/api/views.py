from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer


@api_view(['GET'])
def health(request):
    return Response({"message": "Server is up!"})


# PUBLIC_INTERFACE
@api_view(['GET', 'POST'])
def event_list_create(request):
    """List all events or create a new event."""
    if request.method == 'GET':
        events = Event.objects.all().order_by('date', 'time')
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# PUBLIC_INTERFACE
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def event_detail(request, event_id):
    """Retrieve, update, partially update, or delete an event."""
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        return Response({'detail': 'Event not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventSerializer(event)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = EventSerializer(event, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
