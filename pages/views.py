from django.shortcuts import render

# Create your views here.

def home(request):
    
    template = 'pages/home.html'

    return render(request, template)
