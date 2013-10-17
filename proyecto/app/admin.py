#Para activar el panel
#se debe descomentar en urls.py y settings.py 
#luego crear el archivo admin.py dentro de app
#e ingresamos con /admin
from django.contrib import admin

#from models import *
#es mejor llamar a todos los modelos uno por uno
from models import Enlace, Categoria, Agregador

#CREANDO UN ACTIONS QUE SE CREO EN EL ROOT DEL PROYECTO
from actions import export_as_csv


#AGREGAR COLUMNAS AL ADMIN 
#CREAMOS UN ADMINMODEL
class EnlaceAdmin(admin.ModelAdmin):
	#puede ser un arreglo o una tupla
	#una tupla es mas rapida QUE UNA VELOCIDAD
	
	#list_display = ('titulo','enlace','categoria','votos')
	#list_display = ('titulo','enlace','categoria','mis_votos_en_imagen_rosada')
	#SE PUEDEN CAMBIAR CAMPOR POR FUNCIONES
	list_display = ("id",'titulo','enlace','categoria','imagen_voto',"es_popular")

	#list_filter para navegar mas facil en nuestro listado de elementos
	# normalmente se usa con las claves foraneas 
	list_filter =("categoria","usuario","titulo")

	# para buscar
	#buscar en el titulo de las categorias relacionadas 
	# en las tuplas siempre terminar con una coma si es un solo elemento
	search_fields = ("categoria__titulo","usuario__email")


	def imagen_voto(self, obj):
		url = obj.mis_votos_en_imagen_rosada()
		tag = '<img src="%s">' % url
		return tag

	#en python todos los elementos son objectos
	#a la funcion le dare permiso para usar tags html
	imagen_voto.allow_tags = True

	#las funciones son son ordenables en el adminmodel
	#por ello hay que decirles que campo usar para ordenar
	imagen_voto.admin_order_field = 'votos'

	#PARA QUE FUNCIONE SOLO PUEDO USAR LOS QUE ESTEN EN LIST_DISPLAY
	#Y SOLO CAMPOS , NO FUNCIONES
	list_editable = ("titulo","enlace","categoria")

	#hay un problema volviendo editable el primer cambio del list_display
	#el primer campo no puede ser usado por que siempre lo usa como enlace
	#para poder actualizar
	#en este caso si se quiere poner actualizables el titulo
	#podemos poner como primer campo el id
	#o sino definir  list_display_links = ('es_popular',)
	#list_display_links = ('es_popular',)

	#AGREGAMOS EL ACTION AL ENLACEADMIN
	actions = [export_as_csv]

	#CAMBIANDO EL WIDGET DE LOS CAMPOS FORANEOS
	#para que no los cree como un combobox
	raw_id_fields = ("categoria","usuario")

	#inlines
	#permite controlar modelos  relacionados
	#desde el administrador de un modelo

#MUESTRA EL LISTADO DE OBJECTOS RELACIONADOS A LAS CATEGORIAS
#MAS UN CAMPO PARA AGREGAR OTRO ELEMENTO A ESA CATEGORIA
class EnlaceInline(admin.StackedInline):
	model = Enlace
	#cantidad de forms add de inlines dentro de la edit category
	extra = 1
	#cambiar el widget de un campo dentro del EnlaceInline
	raw_id_fields = ("usuario",)


#creamos una categoria vacia USANDO PASS
class CategoriaAdmin(admin.ModelAdmin):
	#usamos pass cuando queremos cerrar la identacion sin haber agregado algo
	#solo ponemos pass y listo para crear una clase vacia
	#pass	
	inlines = [EnlaceInline]

#creamos un objeto administrador
class AgregadorAdmin(admin.ModelAdmin):
	filter_horizontal = ("enlaces",)
	#tambien tenemos filter_vertical

admin.site.register(Categoria, CategoriaAdmin)

#admin.site.register(Enlace)
# LE DIGO AL MODELO QUE OBJETO USAR
admin.site.register(Enlace,EnlaceAdmin)

admin.site.register(Agregador, AgregadorAdmin)

