from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registrarse/', views.registracion, name='registrarse'),
    path('loguearse/', views.logueo, name='loguearse'),
    path('desloguearse/', LogoutView.as_view(template_name="cuentas/logout.html"), name='desloguearse'),
    path('perfil/', views.editarPerfil, name='perfil'),
    path('avatar/', views.agregarAvatar, name='avatar'),
]