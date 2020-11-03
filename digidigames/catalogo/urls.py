from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Contacto/', views.Contacto, name='Contacto'),
    path('Steam/', views.Steam, name='Steam'),
    path('Origin/', views.Origin, name='Origin'),
    path('Pago/', views.Pago, name='Pago'),
    path('juego/<int:pk>', views.juegoDetailView.as_view(), name='juego-detail')
]

urlpatterns+= [
    path('juego/create/', views.juegoCreate.as_view(), name='juego_create'),
    path('juego/<int:pk>/update/', views.juegoUpdate.as_view(), name='juego_update'),
    path('juego/<int:pk>/delete/', views.juegoDelete.as_view(), name='juego_delete')
]
