from django.test import TestCase
from catalogo.models import Juego

class testmodeljuego (TestCase):

    @classmethod

    def setUpTestData(cls):
        Juego.objects.create(id_juego='1', titulo='Forza Horizon 4', precio='24.900', descipcion='Forza Horizon 4 es un videojuego de carreras de mundo abierto',status='S')
        

    def test_get_absolute_url(self):
        juego=Juego.objects.get(id_juego=1)
        self.assertEquals(juego.get_absolute_url(),'/catalogo/juego/1')

    def test_nombre_label(self):
        juego=Juego.objects.get(id_juego=1)
        field_label = juego._meta.get_field('titulo').verbose_name
        self.assertEquals(field_label,'titulo')

    def test_precio_label(self):
        juego=Juego.objects.get(id_juego=1)
        field_label = juego._meta.get_field('precio').verbose_name
        self.assertEquals(field_label,'precio')

    def test_titulo_max_length(self):
        juego=Juego.objects.get(id_juego=1)
        max_length = juego._meta.get_field('titulo').max_length
        self.assertEquals(max_length,200)
    
    def test_precio_max_length(self):
        juego=Juego.objects.get(id_juego=1)
        max_length = juego._meta.get_field('precio').max_length
        self.assertEquals(max_length,6)

    def test_descripcion_max_length(self):
        juego=Juego.objects.get(id_juego=1)
        max_length = juego._meta.get_field('descipcion').max_length
        self.assertEquals(max_length,1000)

    