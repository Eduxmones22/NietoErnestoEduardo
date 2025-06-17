from django.shortcuts import render, redirect
from cuentas.forms import *
from cuentas.models import Avatar
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
            try:
               avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #______________________________________________________________            
            return render(request, "blog/index.html")
        else:
            return redirect(reverse_lazy('loguearse'))
    else:
        FormLogueo = AuthenticationForm()

    return render(request, "cuentas/login.html", {"form": FormLogueo})

#----------------------------- EDITAR PERFIL ---------------------------
    
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        FormPerfil = Editar_Perfil(request.POST)
        if FormPerfil.is_valid():
            user = User.objects.get(username=usuario)
            user.email = FormPerfil.cleaned_data.get("email")
            user.first_name = FormPerfil.cleaned_data.get("first_name")
            user.last_name = FormPerfil.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("index"))
    else:
        FormPerfil = Editar_Perfil(instance=usuario)
    return render(request, "cuentas/editarPerfil.html", {"form": FormPerfil})

#----------------------------- AGREGAR AVATAR ---------------------------

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        FormAvatar = AvatarForm(request.POST, request.FILES)
        if FormAvatar.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = FormAvatar.cleaned_data["imagen"]
            #_________ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #__________________________________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            #_________ Enviar la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #____________________________________________________
            return redirect(reverse_lazy("index"))
    else:
        FormAvatar = AvatarForm()
    return render(request, "cuentas/agregarAvatar.html", {"form": FormAvatar}) 
    


