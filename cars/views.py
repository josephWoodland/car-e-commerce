from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Car

# Create your views here.

def cars(request):
    car_list = Car.objects.order_by('-created_date')
    paginator = Paginator(car_list, 4 )
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    template = 'cars/cars.html'
    context = {
        'cars': paged_cars,
    }

    return render(request, template, context)


def car_detail(request, id):

    single_car = get_object_or_404(Car, pk=id)
    template = 'cars/car_detail.html'    
    context = {
        'car': single_car,
    }
    
    return render(request, template, context)


def search(request):

    template = 'cars/search.html'

    cars = Car.objects.order_by('-created_date')

    context = {
        'cars' : cars,
    }

    return render( request, template, context )
