from django import forms
from django.forms import ModelForm
from .models import *
import pdb
#empleado,cliente,clienteEmpresa,tipoAbitacion,habitacion
class usuarioform(ModelForm):
 	class Meta:
 		model=usuario
