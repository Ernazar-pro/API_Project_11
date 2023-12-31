from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.viewsets import ModelViewSet
from .serializers import BookingSerializer, HotelSerializer, GuestSerializer, RoomSerializer
from apps.hotel.models import Hotel
from apps.booking.models import Booking
from apps.guest.models import Guest
from apps.room.models import Room
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class GuestViewSet(ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]
