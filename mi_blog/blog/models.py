from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Seccion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

#class Plataformaxs(models.Model):
#    nombre = models.CharField(max_length=100)

#    def __str__(self):
#       return self.nombre


class Consola(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='img_blog/', blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    consola = models.ForeignKey(Consola, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
   
    
    

    def __str__(self):
        return self.titulo
    
class Mensaje(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"De {self.emisor.username} para {self.receptor.username}"
    


