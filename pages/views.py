from django.shortcuts import render

from cars.views import search
from .models import Team
from cars.models import Car
# Create your views here.


def home(request):

    teams = Team.objects.all()
    feature_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')

    # Saving all the unique search terms to add to the drop down list(instead of listing repeated terms)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    
    context = {
        'teams': teams,
        'featured_cars': feature_cars,
        'all_cars': all_cars,
        'model_search' : model_search,
        'city_search' : city_search,
        'body_style_search' : body_style_search,
        'year_search' : year_search,
    }

    template = 'pages/home.html'

    return render(request, template, context)


def about(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }

    template = 'pages/about.html'

    return render(request, template, context)


def services(request):
    
    template = 'pages/services.html'

    return render(request, template)


def contact(request):
    
    template = 'pages/contact.html'

    return render(request, template)
