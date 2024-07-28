from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, "home.html")


def avis(request):
    return render (request, "avis.html")


def menus(request):
    return render (request, "menus.html")


def reservation(request):
    return render (request, "reservation.html")