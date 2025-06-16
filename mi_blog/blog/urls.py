from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('index/', views.index, name='index'),  # Página de inicio
    path('acerca_de_mi/', TemplateView.as_view(template_name="blog/acerca_de_mi.html"), name='acerca_de_mi'),
]