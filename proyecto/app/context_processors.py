#PARA CONFIGURARLO SE MODIFICA EL ARCHVIVO SETTINGS.PY
#GENERA VARIALBES Y FUNCIONES QUE SE PUEDEN USAR EN CUALQUIER 
#PARTE DEL SEISTEMA

from random import choice

from django.core.urlresolvers import reverse

frases = ["leonidas esta sentado","fredie se fue","cris arriba","aaaaaaa","bbbbbb","cccc"]

def ejemplo(request):
	#SE AGREGARA {{frase}} en el template index
	return {"frase":choice(frases)}

def menu(request):
	menu = {"menu":[
		{"name":"home","url":reverse("home")},
		{"name":"add","url":reverse("add")},
		{"name":"About","url":reverse("about")},
	]}
	#PARA RESALTAR UN ITEM DE MENU
	for item in menu["menu"]:
		if request.path == item["url"]:
			item["active"] = True
	return menu
