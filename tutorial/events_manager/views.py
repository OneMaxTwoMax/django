from django.shortcuts import render
from .models import Event
from rest_framework import generics
from .serializers import EventSerializer

class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventCreate(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventUpdate(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDelete(generics.RetrieveDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer