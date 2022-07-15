import email
from django.shortcuts import redirect, render
from .models import Suscribtion


def home(request):
    return render(request, 'index.html')


def success(request):
    return render(request, 'success.html')


def suscribe(request):
    email = request.POST['email']
    Suscribtion.objects.create(email=email)

    return redirect('/success')