from django.shortcuts import render

# Create your views here.

def cars(request):
    

    template = 'cars/cars.html'

    return render(request, template)
