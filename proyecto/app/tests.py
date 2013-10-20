"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#PARA CORRER ESTE TEST USAMOS PYTHON MANAGE.PY TEST APP

from django.test import TestCase

#OBTENEMOS LAS CLASES QUE NECESITMOS PARA LAS PRUEBAS
from .models import Categoria, Enlace
from django.contrib.auth.models import User

#USAMOS REVERSE
from django.core.urlresolvers import reverse



class SimpleTest(TestCase):
    def test_es_popular(self):
    	#si un enlace tiene menos de 11 votos no es popular

    	#creo una categoria para la prueba
		categoria = Categoria.objects.create(titulo="Cat de prueba")

		#creamos un usuario
		usuario = User.objects.create_user(username="Luis",password="lueimg")

		#creamos el enlace
		enlace = Enlace.objects.create(titulo="Prueba",enlace="http://google.com",votos=0,categoria=categoria,usuario=usuario)

		#DIGO A LA PRUEBA QUE ASEGURE QUE ESTOS 2 TIPOS SON IGUALES
		self.assertEqual(enlace.votos,0)

		#llamamos la metodo del enlace
		self.assertEqual(enlace.es_popular(), False)
		#tambien puede escribirse de otra manera
		self.assertFalse(enlace.es_popular())


		#HACEMOS CAMBIOS PARA PRUEBAS
		enlace.votos = 20
		enlace.save()
		#AHORA ESPERAMOS QUE SEA POPULAR
		self.assertEqual(enlace.votos,20)
		self.assertEqual(enlace.es_popular(), True)

	#prueba de vistas para saber si tu pagina esta cargando
    def test_views(self):
    	#se usa client.get para hace una peticion como cliente
		res = self.client.get(reverse("home"))
		self.assertEqual(res.status_code,200)

		res = self.client.get(reverse("about"))
		self.assertEqual(res.status_code,200)

		res = self.client.get(reverse("enlaces"))
		self.assertEqual(res.status_code,200)

		