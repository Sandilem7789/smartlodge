from django.shortcuts import render
from rest_framework import viewsets
from .models import Room, Booking, PMSIntegration
from .serializers import RoomSerializer, BookingSerializer, PMSIntegrationSerializer

# Create your views here.
class RoomViewSet(viewsets.ModelViewSet):                   # ViewSet for Room model
    queryset = Room.objects.all()                           # Get all rooms
    serializer_class = RoomSerializer                       # Use RoomSerializer for serialization
    
class BookingViewSet(viewsets.ModelViewSet):                # ViewSet for Booking model
    queryset = Booking.objects.all()                        # Get all bookings
    serializer_class = BookingSerializer                    # Use BookingSerializer for serialization
    
class PMSIntegrationViewSet(viewsets.ModelViewSet):         # ViewSet for PMSIntegration model
    queryset = PMSIntegration.objects.all()                 # Get all PMS integrations
    serializer_class = PMSIntegrationSerializer             # Use PMSIntegrationSerializer for serialization
