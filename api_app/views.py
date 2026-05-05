from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Event, Registration
from .serializers import EventSerializer

from django.http import HttpResponse

# GET EVENTS (Use Case: View Events)
@api_view(['GET'])
def get_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


# REGISTER EVENT (Use Case: Register Event)
@api_view(['POST'])
def register_event(request):

    user_id = request.data.get('user_id')
    event_id = request.data.get('event_id')

    # DFD: Validate
    if not user_id or not event_id:
        return Response({
            "status": "error",
            "message": "Missing user_id or event_id"
        })

    # DFD: Process
    try:
        user = User.objects.get(id=user_id)
        event = Event.objects.get(id=event_id)
    except:
        return Response({
            "status": "error",
            "message": "User or Event not found"
        })

    # DFD: Check duplicate
    existing = Registration.objects.filter(user=user, event=event).first()
    if existing:
        return Response({
            "status": "error",
            "message": "Already registered"
        })

    # DFD: Save
    Registration.objects.create(user=user, event=event)

    return Response({
        "status": "success",
        "message": "Registered successfully"
    })

def index(request):
    return render(request, 'index.html')


def submit(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        event_id = request.POST.get('event_id')

        try:
            user = User.objects.get(id=user_id)
            event = Event.objects.get(id=event_id)
            Registration.objects.create(user=user, event=event)

            return HttpResponse("Registered successfully")
        except:
            return HttpResponse("Error in registration")