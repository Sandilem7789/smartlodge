from django.contrib import admin
from .models import Room, Booking, PMSIntegration  # Import all models

# Register your models here.
admin.site.register(Room)  # Register the Room model with the admin site
admin.site.register(Booking)  # Register the Booking model
admin.site.register(PMSIntegration)  # Register the PMSIntegration model
