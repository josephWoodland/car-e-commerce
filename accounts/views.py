from django.shortcuts import redirect, render

# Create your views here.

def login(request):

    template = 'accounts/login.html'

    return render(request, template)

def register(request):

    template = 'accounts/register.html'

    return render(request, template)
    
def logout(request):
    return redirect('home')

def dashboard(request):

    template = 'accounts/dashboard.html'

    return render(request, template)
