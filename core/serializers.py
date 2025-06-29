from rest_framework import serializers
from .models import Room, Booking, PMSIntegration

class RoomSerializer(serializers.ModelSerializer): # Serializer for Room model
    class Meta:
        model = Room
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer): # Serializer for Booking model
    class Meta:
        model = Booking
        fields = '__all__'

class PMSIntegrationSerializer(serializers.ModelSerializer): # Serializer for PMSIntegration model
    class Meta:
        model = PMSIntegration
        fields = '__all__'