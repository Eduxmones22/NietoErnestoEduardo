from django.views.generic import CreateView
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 

#from .models import Noticia



class RegistroUsuarios(UserCreationForm):
    email = forms.EmailField(required=False)
    password1 = forms.CharField(label="contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirmar contraseña",widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]        
    
    
class Editar_Perfil(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]   
        
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)           