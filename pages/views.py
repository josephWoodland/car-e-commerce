from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.


def home(request):

    teams = Team.objects.all()
    feature_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    
    context = {
        'teams': teams,
        'featured_cars': feature_cars,
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
