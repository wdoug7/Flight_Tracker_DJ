from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("flight/<int:flight_id>",views.flight, name="flight"),
    path("flight/<int:flight_id>/book", views.book, name="book"),
    path("airport/<int:airport_id>", views.airport,name="airport")

]