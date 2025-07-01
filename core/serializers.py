from rest_framework import serializers
from .models import Room, Booking, PMSIntegration,RoomImage

# RoomImage 
class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['id', 'image', 'caption']

class RoomSerializer(serializers.ModelSerializer): # Serializer for Room model
    class Meta:
        model = Room
        images = RoomImageSerializer(many=True, read_only=True)
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer): # Serializer for Booking model
    class Meta:
        model = Booking
        fields = '__all__'

class PMSIntegrationSerializer(serializers.ModelSerializer): # Serializer for PMSIntegration model
    class Meta:
        model = PMSIntegration
        fields = '__all__'
