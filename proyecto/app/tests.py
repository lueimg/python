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

	#permite crear datos que se usen durante todas las pruebas
	#aqui creamos categorias y usuarios y enlaces
	#setUp se ejecuta antes de todas las pruebas
	def setUp(self):
		#creo una categoria para la prueba
		self.categoria = Categoria.objects.create(titulo="Cat de prueba")

		#creamos un usuario
		self.usuario = User.objects.create_user(username="luis",password="123")

		
	def test_es_popular(self):
    	#si un enlace tiene menos de 11 votos no es popular

    	#creamos el enlace
		enlace = Enlace.objects.create(titulo="Prueba",enlace="http://google.com",votos=0,categoria=self.categoria,usuario=self.usuario)

    	
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


		#CON EL USUARIO CREADO EN SETUP ME LOGEO
		self.assertTrue(self.client.login(username="luis",password="123"))
		#ahora la pagina add deberia funcionar ya que estamos logeados
		#pues si no nos logeamos nos sale redirecion 302 y no es igual a 200 con que estamos comparando
		res = self.client.get(reverse("add"))
		self.assertEqual(res.status_code,200)

    #PRUEBAS A LOS FORMULARIOS
	def test_add(self):
		#TEMENOS QUE LOGEAR A UN USUARIO PRIMERO
		self.assertTrue(self.client.login(username="luis",password="123"))
		#CUENTO QUE NO HAYA ENLACES CREADOS
		self.assertEqual(Enlace.objects.count(), 0)

		#CREO QUE LOS DATOS QUE VOY A ENVIAR COMO POST
		data ={}
		data["titulo"] = "Test titulo"
		#cuando lo guarda django siempre le pone al final "/"
		#por ello es bueno siempre ponerle / al final de una url
		data["enlace"] = "http://google.com/"

		data["categoria"] = self.categoria.id

		#enviamos los datos
		res = self.client.post(reverse("add"), data)
		#revisamos la repuesta
		self.assertEqual(res.status_code, 302)
		self.assertEqual(Enlace.objects.count(),1)

		#obtengo el enlace creado
		enlace = Enlace.objects.all()[0]
		self.assertEqual(enlace.titulo, data["titulo"])
		self.assertEqual(enlace.enlace, data["enlace"])
		self.assertEqual(enlace.categoria, self.categoria)
