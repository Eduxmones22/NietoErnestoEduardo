from django.shortcuts import render, redirect
from cuentas.forms import *
from django.urls import reverse_lazy, reverse

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def registracion(request):
    if request.method == "POST":
       FormRegistro = RegistroUsuarios(request.POST)
       if FormRegistro.is_valid(): 
          FormRegistro.save()
          return redirect(reverse_lazy('index'))
    else:
        FormRegistro = RegistroUsuarios()
    return render(request, "cuentas/registro_usuario.html", {"form":FormRegistro})    

def logueo(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            #_______ Buscar Avatar
            # try:
            #     avatar = Avatar.objects.get(user=request.user.id).imagen.url
            # except:
            #     avatar = "/media/avatares/default.png"
            # finally:
            #     request.session["avatar"] = avatar
            #______________________________________________________________            
            return render(request, "blog/index.html")
        else:
            return redirect(reverse_lazy('loguearse'))
    else:
        FormLogueo = AuthenticationForm()

    return render(request, "cuentas/login.html", {"form": FormLogueo})


