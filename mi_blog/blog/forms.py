from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Consola
from django import forms

class NoticiaForm(forms.Form):
    titulo = forms.CharField(max_length=200, label="Título", required=True, 
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    subtitulo = forms.CharField(max_length=300, label="Subtítulo", required=True, 
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    contenido = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), 
                                label="Contenido", required=True)
    imagen = forms.ImageField(label="Imagen", required=False)
    
    consola = forms.ModelChoiceField(
        queryset=Consola.objects.all(),  # Obtiene todas las consolas de la BD
        label="Consola asociada",
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

