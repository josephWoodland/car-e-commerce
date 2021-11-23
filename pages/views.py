from django.shortcuts import render

# Create your views here.

def home(request):
    
    template = 'pages/home.html'

    return render(request, template)


def about(request):
    
    template = 'pages/about.html'

    return render(request, template)

def services(request):
    
    template = 'pages/services.html'

    return render(request, template)


def contact(request):
    
    template = 'pages/contact.html'

    return render(request, template)
