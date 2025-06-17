from django.urls import path
from . import views
from blog.views import crear_noticia, detalle_noticia,noticias_por_consola
from django.views.generic import TemplateView

urlpatterns = [
    path('index/', views.index, name='index'),  # Página de inicio
    path('noticia/<int:noticia_id>/', detalle_noticia, name='detalle_noticia'),
    path('noticias/consola/<str:nombre>/', noticias_por_consola, name='noticias_por_consola'),
    #path('home/', views.index, name='home'),  # Página de inicio
    # path("crear_noticias/", CrearNoticia.as_view, name="crear_noticias"),
    path("crear_noticias/",  crear_noticia, name="crear_noticias"),
    path('acerca_de_mi/', TemplateView.as_view(template_name="blog/acerca_de_mi.html"), name='acerca_de_mi'),
]