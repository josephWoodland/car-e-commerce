from django.shortcuts import get_object_or_404, render
from .models import Car

# Create your views here.

def cars(request):
    car_list = Car.objects.order_by('-created_date')
    template = 'cars/cars.html'
    context = {
        'cars': car_list,

    }

    return render(request, template, context)


def car_detail(request, id):

    single_car = get_object_or_404(Car, pk=id)
    template = 'cars/car_detail.html'    
    context = {
        'car': single_car,

    }
    
    return render(request, template, context)