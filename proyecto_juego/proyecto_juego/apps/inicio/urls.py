from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto_juego.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'proyecto_juego.apps.inicio.views.home', name='home'),

    url(r'^home$', 'proyecto_juego.apps.inicio.views.home', name='home1'),

    #url(r'^$', 'proyecto_juego.apps.inicio.views.registro', name='registro'),
    #url(r'^$', 'proyecto_juego.apps.inicio.views.home'),
    
    #url(r'^registro/$','proyecto_juego.apps.inicio.views.registro_usuarios', name='registro_usuarios'),
    url(r'^registrar/$','proyecto_juego.apps.inicio.views.registrou', name='registrou'),
    url(r'^ingresar/$','proyecto_juego.apps.inicio.views.ingresar', name='ingresar'),
    url(r'^logout/$',logout_view),
    url(r'^perfil/$',perfil),
    url(r'^active/$',user_active_view),
    url(r'^lista/$',inicio_view),
    url(r'^modificar/$',modificar_view),
    url(r'^npass/$',modificar_pass),
    



    url(r'^tema/$',registro_tema, name='Tema'),
    url(r'^tema/add/(\d+)/$',add_pregunta, name='agregar_pregunta'),
    url(r'^tema/edit/(\d+)/$',ver_preguntas, name='edit_pregunta'),
    url(r'^pregunta/edit/(\d+)/$',edit_pregunta, name='edit_pregunta'),
    url(r'^pregunta/eliminar/(\d+)/$',eliminar_pregunta, name='eliminar_pregunta'),
    #url(r'^registro/pregunta/$',registro_pregunta, name='Pregunta'),
    url(r'^agregar/',agregar, name='agregar_pregunta'),
)

#http://localhost:8000/


