from django.db import models

# Create your models here.
class Room(models.Model):                                           #rooms model
    ROOM_TYPES = [('single', 'Single'),
                  ('double', 'Double'),
                  ('suite', 'Suite'),]
    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES) #room type
    rate = models.DecimalField(max_digits=6, decimal_places=2)  #room rate
    is_available = models.BooleanField(default=True)  #availability of room
    
    def __str__(self):
        return f"{self.name} ({self.room_type})" #string representation of room object