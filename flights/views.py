from django.shortcuts import render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.urls import reverse
from .models import*

def index(request):
    context = Flight.objects.all()
    return render(request, 'index.html', {"context": context})

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404('Flight does not exist.')
    context = {
        'flight': flight,
        'passengers': flight.passengers.all(),
        'non_passenger': Passenger.objects.exclude(flights=flight).all()}

    return render(request, 'flight.html', context)


def book(request, flight_id):
    try:
        passenger_id = int(request.POST['passenger'])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
        return render(request, 'flight/error.html', {'message': 'No selection.'})
    except Passenger.DoesNotExist:
        return render(request, 'flight/error.html', {'message': 'No flight.'})

    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse('flight', args=(flight_id)))