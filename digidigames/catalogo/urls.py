from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('Contacto/', views.Contacto, name='Contacto'),
    path('Steam/', views.Steam, name='Steam'),
    path('Origin/', views.Origin, name='Origin'),
    path('Pago/', views.Pago, name='Pago'),
    path('juego/<str:pk>', views.juegoDetailView.as_view(), name='juego-Detail'),
    path('juegos/', views.juegoListView.as_view(), name='juegos')

]

urlpatterns+= [

    path('juego/create/', views.juegoCreate.as_view(), name='juego_create'),
    path('juego/<str:pk>/update/', views.juegoUpdate.as_view(), name='juego_update'),
    path('juego/<str:pk>/delete/', views.juegoDelete.as_view(), name='juego_delete')

]
