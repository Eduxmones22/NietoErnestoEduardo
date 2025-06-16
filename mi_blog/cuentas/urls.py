from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registrarse/', views.registracion, name='registrarse'),
    path('loguearse/', views.logueo, name='loguearse'),
    path('desloguearse/', LogoutView.as_view(template_name="cuentas/logout.html"), name='desloguearse'), #esta clase ya viene dentro del django, no tengo que hacer un view  
]