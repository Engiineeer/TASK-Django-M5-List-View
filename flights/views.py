from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from flights.models import Flight
from .seializers import FlightsListSerializer, UpcomingBookingSerializer

class FlightsListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightsListSerializer

class UpcomingBookingView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = UpcomingBookingSerializer