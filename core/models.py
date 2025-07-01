from django.db import models
from django.conf import settings                                        # Import settings for user model reference

# Create your models here.
class Room(models.Model):                                               #rooms model
    ROOM_TYPES = [('single', 'Single'),
                ('double', 'Double'),
                ('suite', 'Suite'),]
    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)             #room type
    rate = models.DecimalField(max_digits=6, decimal_places=2)                  #room rate
    is_available = models.BooleanField(default=True)                            #availability of room
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)  # room image
    
    def __str__(self):
        return f"{self.name} ({self.room_type})"                                        #string representation of room object
    
class RoomImage(models.Model):                                                          # Room image model
    room = models.ForeignKey('Room', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.room.name} – {self.caption or 'Image'}"

class Booking(models.Model):                                                            # booking model
    STATUS = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('checked_in', 'Checked In'),
        ('checked_out', 'Checked Out'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)                # Use settings.AUTH_USER_MODEL for user reference
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS, default='confirmed')

    def __str__(self):
        return f"Booking for {self.user.username} in {self.room.name} ({self.status})"

class PMSIntegration(models.Model):                                                             # PMS integration model
    partner_name = models.CharField(max_length=100)
    endpoint = models.URLField()
    auth_token = models.CharField(max_length=255)
    last_synced = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"PMS Integration with {self.partner_name}"

