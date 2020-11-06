from django.db import models
from django.urls import reverse  #Redirecciona una url de un libro al browser 
import uuid                      #se utiliza para definir atributos clave (pk)
# Create your models here.

class Juego(models.Model):
    
    id_juego=models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descipcion= models.TextField(max_length=1000)
    precio=models.CharField(max_length=6)

    LOAN_PLATAFORMA=(
        ('S','Steam'),
        ('O','Origin'),
    )


    status = models.CharField(
        max_length=1,
        choices=LOAN_PLATAFORMA,
        blank=True,
        default='S',
        help_text='Plataforma del juego',
    )

    def get_absolute_url(self):         
        return reverse('juego-Detail', args=[str(self.id_juego)])
    def str(self):         
        return self.titulo
