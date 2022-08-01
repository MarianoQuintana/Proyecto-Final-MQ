from django.db import models
from unittest.util import _MAX_LENGTH

class Empresa(models.Model):
   
    nombre = models.CharField(max_length=255)
    cuit = models.IntegerField()


   

class Empleados(models.Model):

    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    tel = models.IntegerField()
    mail= models.EmailField(max_length=255)
    
    

class Clientes(models.Model):

    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    tel = models.IntegerField()
    mail= models.EmailField(max_length=255)

   
