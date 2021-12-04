from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.

def login(request):

    template = 'accounts/login.html'

    return render(request, template)


def register(request):

    template = 'accounts/register.html'

    if request.method == 'POST':
        messages.error(request, 'This is an error message!!')
        return redirect('register')

    else:
        return render(request, template)


def logout(request):
    return redirect('home')


def dashboard(request):

    template = 'accounts/dashboard.html'

    return render(request, template)
