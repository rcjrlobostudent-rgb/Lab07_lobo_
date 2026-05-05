from django.urls import path
# Make sure these names match EXACTLY what is in your views.py
from .views import event_list, register_event 

urlpatterns = [
    path('events/', event_list),
    path('registrations/', register_event),
]