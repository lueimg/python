# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
#shortcuts
from django.shortcuts import render_to_response,render
#importamos los modelos
from models import *

#PARA ERRORES 404
from django.shortcuts import get_object_or_404

#PARA USAR modelos de FORMAS EN VIEWS
from forms import *

#PARA VALIDAR LAS FORMAS 
from django.template.context import RequestContext

#decoradores para validar logeo de usuarios
# es una funcion que se ejecuta cuando se ejecuta otra funcion
#funciona colocando antes de un def @login_required
from django.contrib.auth.decorators import login_required

""" PARA CREAR UN NUEVO USUARIO python manage.py createsuperuser """

def hora_actual(request):
	"""
	MODO LARGO

	ahora = datetime.now()
	#genero el template
	t = get_template("hora.html")
	#creo las variables del contexto
	c = Context({"hora":ahora, "usuario":"luis"})
	#renderizo el template a html
	html = t.render(c)
	#devuelvo el html
	return HttpResponse(html)

	"""
	now = datetime.now()
	#PROVIENE DE UN SHORTCUTS 
	return render_to_response("hora.html",{"hora":now})

def home(request):
	categorias = Categoria.objects.all()
	
	# enlaces = Enlace.objects.all()   
	""" consulta con orden"""
	enlaces = Enlace.objects.order_by("-votos").all()

	template = "index.html"
	# usar locals() agarra las variables de la funcion y las agrega
	# al contexto
	#locals() es igual que diccionario ={"categorias":categorias,"enlaces":enlaces}
	# locals tambien envia la variable request que contiene al usuario request.user
	#PERO SOLO ENVIA LOS DATOS LOCALES

	#return render_to_response(template,locals())
	
	#PARA ENVIAR LOS DATOS GLOBALES SE DEBE USAR EL SHORTCUT RENDER
	return render(request,template,locals())

@login_required
def plus(req,id_enlace):
	enlace = Enlace.objects.get(pk=id_enlace)
	enlace.votos = enlace.votos + 1
	enlace.save()
	return HttpResponseRedirect("/")

@login_required
def minus(req,id_enlace):
	enlace = Enlace.objects.get(pk=id_enlace)
	enlace.votos = enlace.votos -1
	enlace.save()
	return HttpResponseRedirect("/")

#enlaces de una categoria
def categoria(req,id_cat):
	categorias = Categoria.objects.all()
	#cat= Categoria.objects.get(pk=id_cat)
	# si no existe devuelve un error 404
	cat = get_object_or_404(Categoria,pk=id_cat)
	enlaces = Enlace.objects.filter(categoria = id_cat)

	template = "index.html"
	#return render_to_response(template,locals())
	#AGREGANDO VARIABLES GLOBALES
	return render(request, template.locals())

""" FUNCION PARA QUE LOS USUARIOS CREEN POST"""
@login_required
def add(req):
	#VARIABLE PAR EL TEMPLATE
	categorias = Categoria.objects.all()

	if req.method == "POST":
		form = EnlaceForm(req.POST)
		if form.is_valid():
			"""form.save() #guarda directamente"""
			# Guarda los datos pero aun no lo envia a la BD
			enlace = form.save(commit=False)
			# como escondimos el campo usuario hay que llenarlo dinamicamente
			enlace.usuario = req.user
			#recien guardar
			enlace.save()

			return HttpResponseRedirect("/")
	else:
		form = EnlaceForm()

	template = "form.html"
	return render_to_response(template, context_instance = RequestContext(req,locals()))



