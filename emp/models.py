from django.db import models
from unittest.util import _MAX_LENGTH

class Empresa(models.Model):
   
    nombre = models.CharField(max_length=255)
    cuit = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}:{self.cuit}"


class Empleados(models.Model):

    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    tel = models.IntegerField()
    mail= models.EmailField(max_length=255)
    
    def __str__(self):
        return f"{self.nombre}:{self.edad}:{self.tel}:{self.mail}"

class Clientes(models.Model):

    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    tel = models.IntegerField()
    mail= models.EmailField(max_length=255)

    def __str__(self):
        return f"{self.nombre}:{self.edad}:{self.tel}:{self.mail}"
