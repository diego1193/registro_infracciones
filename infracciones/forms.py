from django import forms
from .models import Infraccion

class InfraccionForm(forms.ModelForm):
    class Meta:
        model = Infraccion
        fields = ['placa_patente', 'timestamp', 'comentarios']  # Los campos que quieres incluir en tu formulario.
        widgets = {
            'timestamp': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Esto permitirá un widget de entrada de fecha y hora.
        }
