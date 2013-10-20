#SE CREA MENDIANTE CLASES
#Y TIENE VARIOS METODOS
# PROCESS_REQUEST , PORCESS_RESPONSE,

#SE TIENE QE REGISTRAR EN EL SETTINGS

from django.shortcuts import redirect
from random import choice

#paises=["Colombia","Mexico","Peru","Panama"]
paises=["Colombia","Peru","Panama"]

def de_donde_vengo(request):
	return choice(paises)

class PaisMiddleware():
	def process_request(self, request):

		pais = de_donde_vengo(request)
		if pais == "Mexico":
			return redirect("http://google.com")

