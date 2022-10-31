from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from flights.models import Flight
from .seializers import FlightsListSerializer, UpcomingBookingSerializer
from django.utils import timezone

class FlightsListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightsListSerializer

class UpcomingBookingView(ListAPIView):
    queryset = Booking.objects.filter(date__gt=timezone.now())
    serializer_class = UpcomingBookingSerializer