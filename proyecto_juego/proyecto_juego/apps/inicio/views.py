from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect 
import datetime
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
import pdb

# Create your views here.
def home(request):	
	#return render_to_response ('base.html',RequestContext(request))
	return render_to_response("base.html",RequestContext(request))

def registro_usuarios(request):
	if request.method=="POST":
		form=UserCreationForm(request.POST)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect("//")
	form=UserCreationForm()
	return render_to_response("usuario/registro.html",{"form":form},RequestContext(request))