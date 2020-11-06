from django.shortcuts import render
from . models import Juego
from django.views import generic

#Importamos informacion para formularios 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request) :
    num_juego = Juego.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_juego':num_juego},
    )

def Contacto(request) :
    num_juego = Juego.objects.all().count()

    return render(
        request,
        'Contacto.html',
        context={'num_juego':num_juego},
    )
def Steam(request) :
    num_juego = Juego.objects.all().count()

    return render(
        request,
        'Steam.html',
        context={'num_juego':num_juego},
    )
def Origin(request) :
    num_juego = Juego.objects.all().count()

    return render(
        request,
        'Origin.html',
        context={'num_juego':num_juego},
    )
def Pago(request) :
    num_juego = Juego.objects.all().count()

    return render(
        request,
        'Pago.html',
        context={'num_juego':num_juego},
    )




#crud

class juegoListView (generic.ListView):
    model = Juego
    paginate_by = 10

class juegoCreate(CreateView):
    model = Juego
    fields = '__all__'

class juegoUpdate(UpdateView):
    model = Juego
    fields = ['titulo', 'descipcion', 'precio',]

class juegoDelete(DeleteView):
    model = Juego
    success_url = reverse_lazy ('index')

class juegoDetailView(generic.DetailView):
    model = Juego