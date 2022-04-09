from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HotelSerializers, GuestSerializers, ReservationSerializers
from rest_framework import generics
from rest_framework import filters
from .models import Hotels, Guest, Reservation
import random


def home(request):
    return HttpResponse("<h1> Hey World!</h1>")


@api_view(['GET', 'POST'])
def hotels_list(request):
    if request.method == 'GET':
        hotel_list = Hotels.objects.all()
        hotelSerializer = HotelSerializers(hotel_list, many=True)
        return Response(hotelSerializer.data)
    if request.method == 'POST':
        hotel_request = request.data
        serialize_request_data = HotelSerializers(data=hotel_request)
        if serialize_request_data.is_valid():
            serialize_request_data.save()
        return Response({"Message": "Added Successfully"})


@api_view(['GET', 'POST'])
def hotels_detail(request, pk):
    if request.method == 'GET':
        hotels_list = Hotels.objects.get(id=pk)
        hotelSerializer = HotelSerializers(hotels_list, many=False)
        return Response(hotelSerializer.data)


class get_generics_list(generics.ListCreateAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


@api_view(['GET'])
def guest_list(request):
    if request.method == 'GET':
        guest_list = Guest.objects.all()
        guest_serializer = GuestSerializers(guest_list, many=True)
        return Response(guest_serializer.data)


@api_view(['GET', 'POST'])
def make_reservation(request):
    if request.method == 'GET':
        reservation = Reservation.objects.all()
        reservation_serializer = ReservationSerializers(reservation, many=True)
        return Response(reservation_serializer.data)
    if request.method == 'POST':
        try:
            reservation_request = request.data
            rrr = random.randint(1000, 9999)
            reservation_request["confirmation_number"] = rrr
            print(reservation_request)
            reservation = Reservation()
            reservation.checkin = reservation_request['checkin']
            reservation.checkout = reservation_request['checkout']
            hotel = Hotels.objects.get(name=reservation_request['hotel'])
            reservation.hotel = hotel
            reservation.confirmation_number = reservation_request['confirmation_number']
            reservation.save()
            reservation.refresh_from_db()
            for guest in reservation_request['guest']:
                guest_model = Guest()
                guest_model.reservation = reservation
                guest_model.guest_name = guest['guest_name']
                guest_model.gender = guest['gender']
                guest_model.save()

            return Response(f'Here is the Confirmation number: {rrr}')
        except Exception as e:
            print(e)
            return Response("Unidentified", status=400)
