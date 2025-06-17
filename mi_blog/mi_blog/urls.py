"""
URL configuration for mi_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views
from cuentas import views
from blog.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #path('index/', index, name='index'),  # Esto carga 'index.html' al iniciar el servidor
    path('blog/', include('blog.urls')),  # Sigue funcionando para /
    
    path('', include('blog.urls')),  # Sigue funcionando para /
    path('index/', include('blog.urls')),  # Ahora también para /index/
    path('cuentas/', include('cuentas.urls')),  # Enlaza las rutas de cuentas  
      
]

# Solo en desarrollo: permite servir archivos en la carpeta media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)