from django.db import models
#TENEMOS QUE CONFIGURAR UNA BD EN SETTINGS.PY
#HAY QUE CREAR LA BD LUEGO DE CREAR LOS MODELOS
#python manage.py syncdb
#luego puedo probar
#python manage.py sqlall app
#SHELL DE DJANGO python manage.py shell

#IMPORTAMOS EL MODELO DE USUARIOS DE DJANGO
from django.contrib.auth.models import User

"""
CREANDO DATOS POR SHELL DE DJANGO

cat = Categoria()
cat.titulo = "python"
cat.save()
//el select * from Categorias 
Categoria.objects.all()

"""
"""
AL HACER UNA EDICION DEL MODELO 
HAY QUE BORRAR EL ARCHIVO DB Y VOLVER A SYNCRONIZAR
"""
"""
USAMOS __UNICODE__ PARA MODIFICAR LA PRESENTACION 
EN EL ADMIN
"""

# Create your models here.
class Categoria(models.Model):
	titulo = models.CharField(max_length = 140)

	def __unicode__(self):
		return self.titulo

class Enlace(models.Model):
	titulo = models.CharField(max_length = 140)
	enlace = models.URLField()
	votos = models.IntegerField(default = 0)
	categoria = models.ForeignKey(Categoria)

	#PARA RELACIONAR A UN USUARIO YA EXISTE UN MODELO USER
	#importamos de django.contrib.auth.models
	usuario = models.ForeignKey(User)
	#usamo la propiedad auto_now_add para que registre la fecha actual
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s - %s " % (self.titulo,self.enlace)

	def mis_votos_en_imagen_rosada(self):
		return "http://placehold.it/200x100/E8117F/FFFFFF/&text=%d+votos" % self.votos

	def es_popular(self):
		return self.votos > 10
	#PODEMOS TRANFORMAR LOS VALORES BOLEANOS EN UNA IMAGEN CHULA :)
	es_popular.boolean = True 

#CUANDO CREAMOS UNA NUEVA CLASE DEVEMOS VOLVER A SYNCRONIZAR
#PYTHON MANAGER.PY SYNCDB
class Agregador(models.Model):
	titulo = models.CharField(max_length=140)
	#CREAMOS UN CAMPO MULTIPLE QUE PUEDE TENER MUCHOS ENLACES
	enlaces = models.ManyToManyField(Enlace)