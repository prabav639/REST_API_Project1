from rest_framework import serializers
from .models import Guest, Hotels, Reservation


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'


class GuestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['guest_name', 'gender']


class ReservationSerializers(serializers.ModelSerializer):
    guest = GuestSerializers(many=True)

    class Meta:
        model = Reservation
        fields = ['hotel', 'checkin', 'checkout', 'guest', 'confirmation_number']

    def create(self, validated_data):
        guests = validated_data.pop('guest')
        reservation = Reservation.objects.create(**validated_data)
        guest_serializer = self.fields['guest']
        for guest in guests:
            guest['reservation'] = reservation
        guest_serializer.create(guests)
        return reservation
