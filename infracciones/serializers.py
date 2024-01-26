from rest_framework import serializers
from .models import Infraccion
import datetime

class InfraccionSerializer(serializers.ModelSerializer):
    def validate_timestamp(self, value):
        if isinstance(value, datetime.datetime):
            # Si el valor ya es un objeto datetime, retórnalo tal cual.
            return value
        try:
            # Intenta convertirlo si es una cadena
            return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            raise serializers.ValidationError("Formato de fecha incorrecto. Usa 'YYYY-MM-DDThh:mm:ssZ'.")


    class Meta:
        model = Infraccion
        fields = ['placa_patente', 'timestamp', 'comentarios']
