from apps.booking.models import Booking
from apps.room.models import Room
from apps.guest.models import Guest
from apps.hotel.models import Hotel
from rest_framework.serializers import *

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class GuestSerializer(ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'

class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

