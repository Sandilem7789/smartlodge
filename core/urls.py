from django.urls import path, include                                   #Import path and include for routing
from rest_framework.routers import DefaultRouter                        # Import DefaultRouter for viewsets
from .views import RoomViewSet, BookingViewSet, PMSIntegrationViewSet   # Import viewsets

router = DefaultRouter()                                                # Create a router instance
router.register(r'rooms', RoomViewSet)                                  # Register RoomViewSet with the router
router.register(r'bookings', BookingViewSet)                            # Register BookingViewSet with the router
router.register(r'pms-integrations', PMSIntegrationViewSet)             # Register PMSIntegrationViewSet with the router

urlpatterns = [                                                                             # Define URL patterns
    path('', include(router.urls)),                                                         # Include the router's URLs
    
]

