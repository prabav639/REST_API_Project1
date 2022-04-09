from django.db import models


class Hotels(models.Model):
    name = models.CharField(max_length=200, null=False, primary_key=True)
    price = models.IntegerField()
    available = models.BooleanField(null=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    confirmation_number = models.CharField(max_length=50, null=True)


class Guest(models.Model):
    reservation = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, related_name='guest')
    guest_name = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=6, null=False)
