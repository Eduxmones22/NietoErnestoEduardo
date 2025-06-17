from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from blog.models import Noticia, Consola
from blog.forms import NoticiaForm

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.
# def index(request):
#     return render(request, 'blog/index.html')

# ------------ MUESTRA LAS ULTIMAS 5 NOTICIAS EN EL HOME -----------------------------
def index(request):
    noticias = Noticia.objects.all().order_by('-fecha')[:5]  # Últimas 5 noticias
    return render(request, "blog/index.html", {"noticias": noticias})

# -----------  REDIRECCIONA A LA PAGINA DE LA NOTICIA SELECCIONADA ------------------

def detalle_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    return render(request, "blog/detalle_noticia.html", {"noticia": noticia})

# -----------  NOTICIA POR CONSOLA ------------------

def noticias_por_consola(request, nombre):
    noticias = Noticia.objects.filter(consola__nombre__iexact=nombre).order_by('-fecha')
    return render(request, 'blog/noticias_por_consola.html', {
        'noticias': noticias,
        'consola': nombre.capitalize()
    })

# -----------  CREA LAS NOTICIAS ------------------
@login_required
def crear_noticia(request):
    if request.method == "POST":
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            noticia = Noticia(
                titulo=form.cleaned_data["titulo"],
                subtitulo=form.cleaned_data["subtitulo"],
                contenido=form.cleaned_data["contenido"],
                imagen=form.cleaned_data.get("imagen", None),
                consola=form.cleaned_data.get("consola", None),
                autor=request.user
            )
            noticia.save()
            return redirect("index")  # Redirigir al inicio después de crear la noticia
    else:
        form = NoticiaForm()

    return render(request, "blog/abm_noticias.html", {"form": form})



