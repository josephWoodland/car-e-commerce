from django.shortcuts import get_object_or_404, render
from .models import Car
# Create your views here.

def cars(request):
    

    template = 'cars/cars.html'

    return render(request, template)


def car_detail(request, id):

    single_car = get_object_or_404(Car, pk=id)
    template = 'cars/car_detail.html'
    context = {
        'car': single_car,

    }
    
    return render(request, template, context)