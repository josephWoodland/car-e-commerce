from django.shortcuts import render
from .models import Team
# Create your views here.


def home(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
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
