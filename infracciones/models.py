from django.db import models

class Infraccion(models.Model):
    placa_patente = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    comentarios = models.TextField()

    def __str__(self):
        return f"Infracción {self.placa_patente} - {self.timestamp}"