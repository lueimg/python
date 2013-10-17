from django import forms
#para crear formularios
from django.forms import ModelForm
#para usar los models de bd
from models import *

"""
PARA USARLO VOY A VIEWS.PY
IMPORT  FROM FORMS IMPORT *

"""
#crearmos una forma llama EnlaceForm
class EnlaceForm(ModelForm):
	#PERMITE DIFINIR DATOS DE UNA CLASE
	class Meta:
		#REUSA LA FORMA DEL MODEL ENLACE
		model = Enlace
		#excluir campos
		exclude = ("votos","usuario",)

