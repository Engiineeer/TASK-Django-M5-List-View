from flights.models import Booking, Flight
from django.contrib import admin

# Register your models here.
admin.site.register([Flight, Booking])