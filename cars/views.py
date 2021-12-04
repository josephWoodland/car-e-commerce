from django.db.models.query_utils import refs_expression
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Car

# Create your views here.

def cars(request):
    car_list = Car.objects.order_by('-created_date')
    paginator = Paginator(car_list, 4 )
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    
    template = 'cars/cars.html'
    context = {
        'cars': paged_cars,
        'model_search' : model_search,
        'city_search' : city_search,
        'body_style_search' : body_style_search,
        'year_search' : year_search,
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

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()
    

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)
    
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)


    context = {
        'cars' : cars,
        'model_search' : model_search,
        'city_search' : city_search,
        'body_style_search' : body_style_search,
        'year_search' : year_search,
        'transmission_search': transmission_search,
    }

    return render( request, template, context )
