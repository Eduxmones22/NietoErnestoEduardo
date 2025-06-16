from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Noticia

class CrearNoticia(LoginRequiredMixin, CreateView):
    model = Noticia
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'consola']
    template_name = 'blog/abm_noticias.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
