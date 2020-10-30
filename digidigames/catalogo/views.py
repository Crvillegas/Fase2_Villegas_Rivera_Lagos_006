from django.shortcuts import render
from . models import juego
from django.views import generic

# Create your views here.
def index(request) :
    num_juego = juego.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_juego':num_juego},
    )
    