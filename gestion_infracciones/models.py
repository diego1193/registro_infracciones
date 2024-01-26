from django.db import models
from django.contrib.auth.models import User

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    placa_patente = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Oficial(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    numero_identificacion = models.CharField(max_length=10, unique=True)

