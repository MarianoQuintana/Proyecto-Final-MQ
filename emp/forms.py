from django import forms

class EmpresaFormulario(forms.Form):
       
    nombre = forms.CharField(max_length=255)
    cuil = forms.IntegerField()

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
