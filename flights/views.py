from .models import Booking, Flight
from rest_framework.generics import ListAPIView ,RetrieveAPIView, CreateAPIView ,RetrieveUpdateAPIView, DestroyAPIView
from flights.models import Flight
from .seializers import FlightsListSerializer, UpcomingBookingSerializer, BookingDetailSerializer, BookingCreateSerializer
from django.utils import timezone

class FlightsListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightsListSerializer

class UpcomingBookingView(ListAPIView):
    queryset = Booking.objects.filter(date__gt=timezone.now())
    serializer_class = UpcomingBookingSerializer

class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class BookingCreateView(CreateAPIView):
    serializer_class = BookingCreateSerializer

class BookingUpdateView(RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingCreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class BookingDeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = UpcomingBookingSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'