from django import forms
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class EmpresaFormulario(forms.Form):
       
    nombre = forms.CharField(max_length=255)
    cuit = forms.IntegerField()

class EmpleadosFormulario(forms.Form):

    nombre = forms.CharField(max_length=255)
    edad = forms.IntegerField()
    tel = forms.IntegerField()
    mail= forms.EmailField(max_length=255)

class ClientesFormulario(forms.Form):

    nombre = forms.CharField(max_length=255)
    edad = forms.IntegerField()
    tel = forms.IntegerField()
    mail= forms.EmailField(max_length=255)

class Busqueda_Clientes(forms.Form):
    criterio = forms.CharField(max_length=40)