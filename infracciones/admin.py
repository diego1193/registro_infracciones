from django.contrib import admin
from .models import Infraccion
from gestion_infracciones.admin import my_admin_site

@admin.register(Infraccion, site=my_admin_site)
class InfraccionAdmin(admin.ModelAdmin):
    list_display = ('placa_patente', 'timestamp', 'comentarios')
    search_fields = ('placa_patente', 'comentarios')
