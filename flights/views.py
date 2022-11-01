from datetime import datetime
from .models import Booking, Flight
from rest_framework.generics import ListAPIView ,RetrieveAPIView ,RetrieveUpdateAPIView, DestroyAPIView
from flights.models import Flight
from .seializers import FlightsListSerializer, BookinglistSerializer, BookingDetailSerializer, BookingupdateSerializer


class FlightsListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightsListSerializer

class BookingListView(ListAPIView):
    queryset = Booking.objects.filter(date__gt=datetime.today())
    serializer_class = BookinglistSerializer

class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'



class BookingUpdateView(RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingupdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class BookingDeleteView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookinglistSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'