from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from blog.models import Noticia, Consola
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

class CrearNoticia(LoginRequiredMixin, CreateView):
    model = Noticia
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'consola']
    template_name = 'pages/crear_noticia.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
