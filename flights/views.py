from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Flight, Passenger, Airport

# Create your views here.
def airport(request, airport_id):
    try:
        airport = Airport.objects.get(pk=airport_id)
    except Airport.DoesNotExist:
        raise Http404("Airport does not exist")
    context = {
    "airport": airport
    }
    return render(request, 'flights/airport.html)',context)




def index(request):
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, 'flights/index.html', context)

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")
    context = {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    }
    return render(request, 'flights/flight.html', context)

def book (request, flight_id):
    try:
        passenger_id = int(request.POST['passenger'])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
        return render(request, "flights/error.html", {"message":"No Selection"})
    except Flight.DoesNotExist:
        return render(request, "flights/error.html", {"message":"No Flight"})
    except Passenger.DoesNotExist:
        return render(request, "flights/error.html", {"message":"No Passenger"})
    
    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))