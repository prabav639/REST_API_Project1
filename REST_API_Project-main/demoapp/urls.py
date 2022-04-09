from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("hotel_list/", views.hotels_list, name="hotelsList"),
    path("generics_hotel_list/", views.get_generics_list.as_view(), name="genericsList"),
    path("guest_list/", views.guest_list),
    path("reservation/", views.make_reservation)

]
