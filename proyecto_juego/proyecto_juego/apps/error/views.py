from django.shortcuts import render,render_to_response
from django.template import RequestContext
# Create your views here.
def error_permisos(request):
	return render_to_response("error/error_permisos.html",{},RequestContext(request))
